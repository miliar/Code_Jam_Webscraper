#include <iostream>
#include <set>
#include <sstream>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <thread>
#include <mutex>
#include <map>

using namespace std;
std::mutex output_lock;

char w[111111];

class TSolver {
private:
    map<string, int> q;

    int id(const string& s) {
        auto it = q.find(s);
        if (it == q.end()) {
            int num = q.size();
            q[s] = num;
            return num;
        }
        return it->second;
    }

    vector<vector<int>> a;
    vector<int> A[2];
    int IT = 0;
    int n;
    int ans = 1e9;
private:
    void doInputData() {
        scanf("%d\n", &n);
        a.resize(n);
        for (int i = 0; i < n; ++i) {
            gets(w);
            stringstream ss(w);
            string word;
            while (ss >> word) {
                a[i].push_back(id(word));
            }
        }
    }

    void doSolve() {
        A[0].resize(q.size());
        A[1].resize(q.size());

        int lim = 1 << n;
        for (int msk = 0; msk < lim; ++msk) {
            ++IT;
            if ((msk & 1) || !(msk & 2)) continue;
            for (int i = 0; i < n; ++i) {
                vector<int>& cur = (msk & (1 << i)) ? A[0] : A[1];
                for (int x : a[i]) {
                    cur[x] = IT;
                }
            }

            int cand = 0;
            for (size_t i = 0; i < A[0].size(); ++i)
                if (A[0][i] == IT && A[1][i] == IT) ++cand;
            ans = min(ans, cand);
        }
    }

    void doOuptutData() {
        cout << ans << endl;
    }

public:
    void inputData() {
        doInputData();
        {
            std::lock_guard<std::mutex> lock(output_lock);
            cerr << "[#" << testNo << "]: input data finished\n";
        }
    }

    void solve() {
        doSolve();
        {
            std::lock_guard<std::mutex> lock(output_lock);
            cerr << "[#" << testNo << "]: solving finished\n";
        }
    }

    void outputData() {
        printf("Case #%d: ", testNo);
        doOuptutData();
    }

    void setTestNo(int number) {
        testNo = number;
    }
private:
    int testNo;
};

vector<TSolver> solvers;
queue<int> unsolved;
std::mutex queue_lock;

void worker() {
    while (true) {
        int testNo = -1;
        {
            std::lock_guard<std::mutex> lock(queue_lock);
            if (unsolved.empty()) {
                return;
            }
            testNo = unsolved.front();
            unsolved.pop();
        }
        solvers[testNo].solve();

    }
}

int main() {
    int T;
    scanf("%d\n", &T);

    solvers.resize(T);
    for (int i = 0; i < T; ++i) {
        solvers[i].setTestNo(i + 1);
        solvers[i].inputData();
        unsolved.push(i);
    }

#ifdef DEBUG
    const size_t THREAD_COUNT = 1;
#else
    const size_t THREAD_COUNT = 4;
#endif
    std::vector<std::thread> workers;
    for (size_t i = 0; i < THREAD_COUNT; ++i) {
        workers.emplace_back(worker);
    }
    for (auto& worker : workers) {
        worker.join();
    }

    for (auto& solver : solvers) {
        solver.outputData();
    }

    return 0;
}

