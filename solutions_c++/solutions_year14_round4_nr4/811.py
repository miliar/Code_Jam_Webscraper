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

#define MOD 1000000007

using namespace std;

#define PROBLEM "D"

class TestCaseSolver {
    std::stringstream sout;
    // own vars
    LL n, servers;
    vector<string> s;
public:
    void read();
    void solve();
    void print() {
        std::cout << sout.str() << std::flush;
    }
    void cluster();
};

void TestCaseSolver::read() {
    cin >> n >> servers;
    s.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }
}

void TestCaseSolver::solve() {
    uLL max_mask = 1;
    for (int i = 0; i < n; ++i) {
        max_mask *= servers;
    }
    LL best_res = numeric_limits<LL>::min();
    LL best_occ = 0;
    for (uLL mask = 0; mask < max_mask; ++mask) {
        vector<unordered_set<string>> data(servers);
        uLL t_mask = mask;
        for (auto &str : s) {
            LL cur_server = t_mask % servers;
            for (int i = 0; i <= str.length(); ++i) {
                data[cur_server].insert(str.substr(0, i));
            }
            t_mask /= servers;
        }
        LL res = 0;
        for (int i = 0; i < data.size(); ++i) {
            res += data[i].size();
        }
        if (res > best_res) {
            best_res = res;
            best_occ = 1;
        } else if (res == best_res) {
            ++best_occ;
        }
    }
    sout << (best_res % MOD) << " " << (best_occ % MOD) << endl;
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