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

#define PROBLEM "B"

class TestCaseSolver {
    std::stringstream sout;
    // own vars
    LL n;
    vector<LL> src;
public:
    void read();
    void solve();
    void print() {
        std::cout << sout.str() << std::flush;
    }
    void cluster();
};

void TestCaseSolver::read() {
    cin >> n;
    src.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> src[i];
    }
}

void TestCaseSolver::solve() {
    LL best_res = numeric_limits<LL>::max();
    int max_bm = (1ULL << n);
    for (uLL bm = 0; bm < max_bm; ++bm) {
        LL cur_res = 0;
        vector<LL> left;
        vector<LL> right;
        uLL bm_t = bm;
        for (int i = 0; i < n; ++i) {
            if (bm_t & 1) {
                left.push_back(src[i]);
            } else {
                right.push_back(src[i]);
            }
            bm_t >>= 1;
        }
        sort(left.begin(), left.end());
        sort(right.rbegin(), right.rend());
        left.insert(left.end(), right.begin(), right.end());
        auto &tmp = left;
        for (int i = 0; i < n; ++i) {
            LL req = src[i];
            int pos = std::find(tmp.begin(), tmp.end(), req) - tmp.begin();
            for (int j = pos; j > i; --j) {
                std::swap(tmp[j], tmp[j - 1]);
                ++cur_res;
            }
        }
        best_res = min(cur_res, best_res);
        if (tmp != src) {
            throw runtime_error("Assertion failed: different vectors in the end");
        }
    }
    sout << best_res << endl;
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