#define _CRT_SECURE_NO_WARNINGS

#include <thread>
#include <condition_variable>
#include <mutex>

#include <memory>

#include <vector>
#include <queue>

#include <cstdio>

#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <iostream>
#include <assert.h>
#include <chrono>
using namespace std;

#pragma comment(linker, "/STACK:16777216")

typedef long long ll;
typedef pair<int, int> pii;

const int INF = 1e9;
const double EPS = 1e-9;
const double PI = acos(-1.);

struct TResult {
    ll res;
    void PrintToStdout(int index) {
        printf("Case #%d: ", (int)(index + 1));
        if (res == -1)
            puts("IMPOSSIBLE");
        else
            printf("%lld\n", res);
    }
};

char arr[] = "<>^v";

struct TInput {
    int n, m;
    char M[110][110];
    void ReadFromStdin() {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", M[i]);
        }
    }

    bool check(int x, int y) {
        int dx = 0;
        int dy = 0;
        if (M[x][y] == '^')
            dx = -1;
        if (M[x][y] == 'v')
            dx = 1;

        if (M[x][y] == '<')
            dy = -1;
        if (M[x][y] == '>')
            dy = 1;
        x += dx;
        y += dy;
        while (x >= 0 && x < n && y >= 0 && y < m) {
            if (M[x][y] != '.')
                return true;
            x += dx;
            y += dy;
        }
        return false;
    }

    void Run(TResult& result) {
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (M[i][j] == '.')
                    continue;
                if (check(i, j))
                    continue;
                bool f = false;
                for (int k = 0; k < 4; ++k) {
                    M[i][j] = arr[k];
                    if (check(i, j))
                        f = true;
                }
                if (f)
                    ++ans;
                else {
                    result.res = -1;
                    return;
                }
            }
        }
        result.res = ans;
    }

    bool operator < (const TInput& other) {
        return false;          // in oreder of input
//        return n < other.n;    // start with biggest n
    }
};

const size_t THREAD_COUNT = 1;
const size_t MAX_BUCKETS = 100;
const size_t AUTO_UPDATE_MILLISECONDS = 1000; // 0 to turnoff
const size_t UPDATES_COUNT = 1000; // do O(UPDATES_COUNT) printings of progress on test solving

typedef shared_ptr<TResult> TResultPtr;
typedef shared_ptr<TInput> TInputPtr;

class TProgressPrinter {
    size_t SolvedCount;
    size_t TestsCount;
    string Progress;
    mutex Sync;
    size_t BucketSize;
    vector<size_t> CntInBucket;
    chrono::time_point<chrono::high_resolution_clock> startTime;
    bool Running;
    unique_ptr<thread> UpdatingThread;
    size_t UpdateStep;
    size_t EventsCnt;

public:
    TProgressPrinter(size_t testsCount)
        : SolvedCount(0)
        , TestsCount(testsCount)
        , startTime(chrono::high_resolution_clock::now())
        , Running(false)
        , EventsCnt(0)
    {
        BucketSize = (testsCount + MAX_BUCKETS - 1) / MAX_BUCKETS;
        size_t bucketsCnt = (testsCount + BucketSize - 1) / BucketSize;
        Progress.resize(bucketsCnt, ' ');
        CntInBucket.resize(bucketsCnt, BucketSize);
        if (bucketsCnt*BucketSize > testsCount) {
            CntInBucket.back() = testsCount - (bucketsCnt - 1)*BucketSize;
        }
        UpdateStep = testsCount/UPDATES_COUNT + 1;
    }

    void RunUpdating() {
        while(Running) {
            PrintProgress();
            this_thread::sleep_for(chrono::milliseconds(AUTO_UPDATE_MILLISECONDS));
        }
    }

    void OnStart() {
        PrintProgress();
        Running = true;
        if (AUTO_UPDATE_MILLISECONDS)
            UpdatingThread.reset(new thread(&TProgressPrinter::RunUpdating, this));
    }

    void OnJobStart(size_t jobId) {
        bool needUpdate = false;
        {
            lock_guard<mutex> g(Sync);
            size_t bucketNumber = jobId / BucketSize;
            Progress[bucketNumber] = '.';
            ++EventsCnt;
            needUpdate = EventsCnt%UpdateStep == 0;
        }
        if (needUpdate)
            PrintProgress();
    }

    void OnJobFinish(size_t jobId) {
        bool needUpdate = false;
        {
            lock_guard<mutex> g(Sync);
            size_t bucketNumber = jobId / BucketSize;
            --CntInBucket[bucketNumber];
            if (CntInBucket[bucketNumber] == 0)
                Progress[bucketNumber] = '#';
            ++SolvedCount;
            ++EventsCnt;
            needUpdate = EventsCnt%UpdateStep == 0;
        }
        if (needUpdate)
            PrintProgress();
    }

    void PrintProgress() {
        lock_guard<mutex> g(Sync);
        auto curTime = chrono::high_resolution_clock::now();
        size_t elapsed = chrono::duration_cast<std::chrono::milliseconds>(curTime - startTime).count();
        int minutes = elapsed / 60000;
        int seconds = (elapsed / 1000) % 60;
        int milliseconds = elapsed % 1000;
        fprintf(stderr, "\r%2d:%02d.%03d %6d [%s]", minutes, seconds, milliseconds, (int)SolvedCount, Progress.c_str());
    }

    void OnFinish() {
        Running = false;
        PrintProgress();
        if (AUTO_UPDATE_MILLISECONDS)
            UpdatingThread->join();
        fprintf(stderr, "\n");
    }
};

class TResultQueue {
    struct TResultQueueItem {
        TResultPtr Result;
        size_t Index;

        TResultQueueItem(const TResultPtr& result, size_t index)
            : Result(result)
            , Index(index)
        {
        }

        bool operator < (const TResultQueueItem& other) const {
            return Index > other.Index;
        }
    };

    size_t NextIndex;
    priority_queue<TResultQueueItem> ResultQueue;
    mutex Sync;

public:
    TResultQueue()
        : NextIndex(0)
    {}

    void Push(TResultPtr result, size_t index) {
        lock_guard<mutex> g(Sync);
        ResultQueue.push(TResultQueueItem(result, index));
        while (ResultQueue.size() > 0 && ResultQueue.top().Index == NextIndex) {
            TResultQueueItem item = ResultQueue.top();
            item.Result->PrintToStdout(item.Index);
            ++NextIndex;
            ResultQueue.pop();
        }
    }
};

class TJobQueue {
    struct TInputQueueItem {
        TInputPtr Input;
        size_t Index;

        TInputQueueItem()
        {}

        TInputQueueItem(const TInputPtr& input, size_t index)
            : Input(input)
            , Index(index)
        {
        }

        bool operator < (const TInputQueueItem& other) const {
            if (*Input < *other.Input)
                return true;
            if (*other.Input < *Input)
                return false;
            return Index > other.Index;
        }
    };
    priority_queue<TInputQueueItem> InputQueue;
    bool IsRunning;
    size_t JobIndex;

    typedef shared_ptr<thread> TThreadPtr;
    vector<TThreadPtr> Threads;

    mutex Sync;

    TResultQueue ResultQueue;
    TProgressPrinter progressPrinter;

    void operator() () {
        TInputQueueItem job;
        while (GetNewJob(job)) {
            progressPrinter.OnJobStart(job.Index);
            TResultPtr result(new TResult);
            job.Input->Run(*result);
            ResultQueue.Push(result, job.Index);
            progressPrinter.OnJobFinish(job.Index);
        }
    }

    bool GetNewJob(TInputQueueItem& resJob) {
        lock_guard<mutex> g(Sync);
        if (InputQueue.empty())
            return false;
        resJob = InputQueue.top();
        InputQueue.pop();
        return true;
    }

public:
    TJobQueue(size_t testsCount)
        : IsRunning(false)
        , JobIndex(0)
        , progressPrinter(testsCount)
    {
    }

    void Push(TInputPtr input) {
        assert(!IsRunning);
        InputQueue.push(TInputQueueItem(input, JobIndex));
        ++JobIndex;
    }

    void Run(size_t threadCount) {
        IsRunning = true;
        progressPrinter.OnStart();
        if (threadCount == 1) {
            (*this)();
        } else {
            for (size_t i = 0; i < threadCount; ++i) {
                Threads.push_back(TThreadPtr(new thread(&TJobQueue::operator(), this)));
            }
            for (const auto& t : Threads) {
                t->join();
            }
        }
        progressPrinter.OnFinish();
    }
};

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    TJobQueue jobQueue(T);
    for (int i = 0; i < T; ++i) {
        TInputPtr in(new TInput);
        in->ReadFromStdin();
        jobQueue.Push(in);
    }
    jobQueue.Run(THREAD_COUNT);
    return 0;
}
