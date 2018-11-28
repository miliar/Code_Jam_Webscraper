#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>

#include <algorithm>
#include <cmath>
#include <ctime>

#include <stack>
#include <deque>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

#include <future>

#define uLL unsigned long long
#define LL long long
#define BIG 1000000000

using namespace std;

#define PROBLEM "A"

class TestCaseSolver {
    std::stringstream sout;
    // own vars
    LL n, max_size;
    vector<LL> files;
public:
    void read();
    void solve();
    void print() {
        std::cout << sout.str() << std::flush;
    }
    void cluster();
};

void TestCaseSolver::read() {
    cin >> n >> max_size;
    for (int i = 0; i < n; ++i) {
        LL x;
        cin >> x;
        files.push_back(x);
    }
}

void TestCaseSolver::solve() {
    int res = 0;
    sort(files.rbegin(), files.rend());
    vector<bool> used(files.size());
    for (int i = 0; i < files.size(); ++i) {
        if (used[i]) {
            continue;
        }
        used[i] = true;
        ++res;
        int best = -1;
        for (int j = 0; j < files.size(); ++j) {
            if (!used[j] && files[i] + files[j] <= max_size) {
                best = j;
                break;
            }
        }
        if (best != -1) {
            used[best] = true;
        }
    }
    sout << res << endl;
}

int main() {
    srand(unsigned(time(0)));
    if (
        !freopen("input_" PROBLEM ".txt", "rt", stdin) ||
        !freopen("output.txt", "wt", stdout)
        ) {
        std::cerr << "Couldn't open files." << std::endl;
    }
    int num_tests;
    cin >> num_tests;
    std::vector<std::future<TestCaseSolver *>> solver_futures;
#ifdef _DEBUG
    auto launch_type = std::launch::deferred;
#else
    auto launch_type = std::launch::async;
#endif
    for (int i = 0; i < num_tests; ++i) {
        auto *solver = new TestCaseSolver();
        solver->read();
        solver_futures.push_back(std::async(launch_type,
            [solver, i]() -> TestCaseSolver * {
            solver->solve();
            return solver;
        }
        ));
    }
    for (uLL i = 0; i < num_tests; ++i) {
        cerr << "Now solving: " << (i + 1) << "\r" << flush;
        cout << "Case #" << (i + 1) << ": ";
        auto *solver = solver_futures[i].get();
        solver->print();
        delete solver;
    }
    return 0;
}