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

#define Graph vector<vector<pair<int, int>>>

using namespace std;

#define PROBLEM "C"

class TestCaseSolver {
    std::stringstream sout;
    // own vars
    int w, h;
    vector<vector<bool>> river;
public:
    void read();
    void solve();
    void print() {
        std::cout << sout.str() << std::flush;
    }
    inline int r1(int y, int x) {
        return 2 * (y * w + x);
    }
    inline int r2(int y, int x) {
        return 2 * (y * w + x) + 1;
    }
    inline int from() {
        return r1(h, 0);
    }
    inline int to() {
        return r2(h, 0);
    }
};

void TestCaseSolver::read() {
    cin >> w >> h;
    int n;
    cin >> n;
    river.resize(h);
    for (int i = 0; i < h; ++i) {
        river[i].resize(w);
    }
    for (int i = 0; i < n; ++i) {
        int x_0, y_0, x_1, y_1;
        cin >> x_0 >> y_0 >> x_1 >> y_1;
        for (int i = y_0; i <= y_1; ++i) {
            for (int j = x_0; j <= x_1; ++j) {
                river[i][j] = true;
            }
        }
    }
}

bool find_path(vector<int> &res, const Graph &flows, int FROM, int TO) {
    res.clear();
    queue<int> q;
    unordered_set<int> used;
    unordered_map<int, int> from;
    q.push(FROM);
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (cur == TO) {
            res.push_back(cur);
            while (cur != FROM) {
                cur = from[cur];
                res.push_back(cur);
            }
            reverse(res.begin(), res.end());
            return true;
        }
        for (auto &adj : flows[cur]) {
            if (adj.second <= 0 || used.count(adj.first)) {
                continue;
            }
            used.insert(adj.first);
            q.push(adj.first);
            from[adj.first] = cur;
        }
    }
    return false;
}

void TestCaseSolver::solve() {
    Graph flows(2 * w * h + 2 + 10);
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (i + 1 < h && !river[i][j] && !river[i + 1][j]) {
                flows[r2(i, j)].push_back(make_pair(r1(i + 1, j), 1));
                flows[r2(i + 1, j)].push_back(make_pair(r1(i, j), 1));
                flows[r1(i, j)].push_back(make_pair(r2(i + 1, j), 0));
                flows[r1(i + 1, j)].push_back(make_pair(r2(i, j), 0));
            }
            if (j + 1 < w && !river[i][j] && !river[i][j + 1]) {
                flows[r2(i, j)].push_back(make_pair(r1(i, j + 1), 1));
                flows[r2(i, j + 1)].push_back(make_pair(r1(i, j), 1));
                flows[r1(i, j)].push_back(make_pair(r2(i, j + 1), 0));
                flows[r1(i, j + 1)].push_back(make_pair(r2(i, j), 0));
            }
        }
    }
    int FROM = from();
    int TO = to();
    for (int i = 0; i < w; ++i) {
        flows[FROM].push_back(make_pair(r1(0, i), 1));
        flows[r1(0, i)].push_back(make_pair(FROM, 0));
        flows[r2(h - 1, i)].push_back(make_pair(TO, 1));
        flows[TO].push_back(make_pair(r2(h - 1, i), 0));
    }
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            flows[r1(i, j)].push_back(make_pair(r2(i, j), 1));
            flows[r2(i, j)].push_back(make_pair(r1(i, j), 0));
        }
    }
    vector<int> path;
    while (find_path(path, flows, FROM, TO)) {
        for (int i = 0; i < path.size() - 1; ++i) {
            int cur = path[i];
            int nxt = path[i + 1];
            int idx = 0;
            while (flows[cur][idx].first != nxt) {
                ++idx;
            }
            --flows[cur][idx].second;
            idx = 0;
            while (flows[nxt][idx].first != cur) {
                ++idx;
            }
            ++flows[nxt][idx].second;
        }
    }
    int res = 0;
    for (auto &x : flows[FROM]) {
        res += 1 - x.second;
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