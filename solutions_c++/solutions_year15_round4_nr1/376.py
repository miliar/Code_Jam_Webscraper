#include <iostream>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <thread>
#include <mutex>

using namespace std;
std::mutex output_lock;

class TSolver {
private:
    vector<string> a;
    int n, m;

    int ans = 0;
private:
    void doInputData() {
        scanf("%d%d\n", &n, &m);
        a.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
    }

    void doSolve() {
        ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                char c = a[i][j];
                if (c == '.') continue;

                int dx = 0, dy = 0;
                if (c == '>') dy = 1;
                if (c == '<') dy = -1;
                if (c =='^') dx = -1;
                if (c == 'v') dx = 1;

                int cx = i, cy = j;
                cx += dx; cy += dy;

                bool cool = false;
                while (cx >= 0 && cx < n && cy >= 0 && cy < m) {
                    if (a[cx][cy] != '.') {
                        cool = true;
                        break;
                    }
                    cx += dx; cy += dy;
                }

                if (!cool) {
                    for (int x = 0; x < n; ++x)
                        if (x != i && a[x][j] != '.') {
                            cool = true;
                            break;
                        }
                    for (int y = 0; y < m; ++y)
                        if (y != j && a[i][y] != '.') {
                            cool = true;
                            break;
                        }
                    if (cool) ++ans;
                    else {
                        ans = -1;
                        return;
                    }
                }
            }
    }

    void doOuptutData() {
        if (ans == -1) puts("IMPOSSIBLE");
        else
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

