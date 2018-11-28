#include <iostream>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <thread>
#include <mutex>

using namespace std;
std::mutex output_lock;
const double eps = 1e-6;

class TSolver {
private:
    int n;
    vector<double> r, c;
    double v, x;

    bool cool = true;
    double ans;
private:
    void doInputData() {
        cin >> n >> v >> x;
        r.resize(n); c.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> r[i] >> c[i];
        }
    }

    void doSolve() {
        cool = true;
        if (n == 2) {
            if (fabs(c[0] - c[1]) < eps) {
                n = 1;
                r[0] += r[1];
            }
        }

        if (n == 1) {
            if (fabs(c[0] - x) > eps) {
                cool = false;
                return;
            }
            ans = v / r[0];
            return;
        }

        if (max(c[0], c[1]) + eps < x || min(c[0], c[1]) - eps > x) {
            cool = false;
            return;
        }

        double a1 = r[0] * c[0], b1 = r[1] * c[1], c1 = x * v;
        double a2 = r[0], b2 = r[1], c2 = v;

        double d = a1 * b2 - a2 * b1;
        double t1 = (c1 * b2 - c2 * b1) / d;
        double t2 = (a1 * c2 - a2 * c1) / d;

        ans = max(t1, t2);
    }

    void doOuptutData() {
        if (!cool) puts("IMPOSSIBLE");
        else {
            cout.precision(15); cout << fixed;
            cout << ans << endl;
        }
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

