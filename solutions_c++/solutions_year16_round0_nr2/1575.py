

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <fstream>
#include <future>
#include <thread>
#include <chrono>
#include <iomanip>
#include <thread>
#include <atomic>

using namespace std;
typedef int64_t int64;

typedef pair<int,int> pii;
typedef pair<double,double> pdd;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define all(x) (x).begin(), (x).end()

template<typename T>
int nextValue(std::istream & in) {
    T i;
    in >> i;
    return i;
}

template<typename T>
std::vector<T> readVector(std::istream &in, int n) {
    std::vector<T> c;
    std::generate_n(std::back_inserter(c), n, [&in](){ return nextValue<T>(in); });
    return c;
}

std::chrono::time_point<std::chrono::system_clock> now() { return std::chrono::system_clock::now(); }
double since(const std::chrono::time_point<std::chrono::system_clock> &t0)
    { return std::chrono::duration<double>(std::chrono::system_clock::now() - t0).count(); }

static int64 gcd(int64 a, int64 b) {
    if (a < 0 || b < 0)
        return -1;
    while (b != 0) {
        int64 x = a % b;
        a = b;
        b = x;
    }
    return a;
}

class SolverBase {
    std::ostringstream out_;
public:
    virtual void read(std::istream & in) = 0;
    virtual void solve() { saw(out_); }
    virtual void write(std::ostream & out) { out << out_.str(); }
    string str() { return out_.str(); }
    operator string() { return out_.str(); }

protected:
    virtual void saw(std::ostream & out) = 0;	// solve and write
};

map<vector<char>, int> minFlips;

static char flip(char c) {
    return ('-' + '+') - c;
}

static vector<char> flip(vector<char> const & a, int k) {
    vector<char> r(a.size());
    for (int i = 0; i < k; ++i) {
        r[i] = flip(a[k - i - 1]);
    }
    for (int i = k; i < a.size(); ++i) {
        r[i] = a[i];
    }
    return r;
}

static void follow(vector<char> const & a, int cost) {
    auto const &loc = minFlips.find(a);
    if (loc == minFlips.end() || loc->second > cost) {
        minFlips[a] = cost;
        for (int i = 1; i <= a.size(); ++i) {
            auto b = flip(a, i);
            follow(b, cost + 1);
        }
    }
}


static void solveAll(int nn) {
    for (int j = 1; j <= nn; j++) {
        vector<char> a;
        for (int i = 0; i < j; ++i) {
            a.push_back('+');
        }
        follow(a, 0);
    }
}

class Solver : public SolverBase {
    vector<char> a_;
public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);

};


void Solver::read(std::istream &in) {
    string s;
    getline(in >> std::ws, s);
    for (auto c : s) {
        a_.push_back(c);
    }
}

static int solve1(vector<char> const & a, int n, char goal) {
    int k = n;
    while (k > 0 && a[k-1] == goal)
        k--;
    if (k == 0)
        return 0;
    if (a[0] != goal)
        return 1 + solve1(a, k, flip(goal));
    int m = 0;
    while (m < k && a[m] == goal)
        m++;
    auto b = flip(a, m);
    return 2 + solve1(b, k, flip(goal));
}

void testAll(int n) {
    int nn = 1 << n;
    for (int i = 0; i < nn; ++i) {
        vector<char> a;
        int k = i;
        for (int j = 0; j < n; ++j) {
            a.push_back(k % 2 == 0 ? '-' : '+');
            k /= 2;
        }
        int p = solve1(a, n, '+');
        int q = minFlips[a];
        if (p != q) {
            std::copy(a.begin(), a.end(), std::ostream_iterator<char>(std::cerr, " "));
            cerr << endl;
            cerr.flush();
            throw 1;
        }
    }
}

void Solver::saw(std::ostream &out) {
    //out.precision(9);
    int best = solve1(a_, int(a_.size()), '+');
//    if (best != minFlips[a_]) {
//        std::copy(a_.begin(), a_.end(), std::ostream_iterator<char>(std::cerr, " "));
//        cerr << endl;
//        cerr.flush();
//        throw 1;
//    }
    out << best;
}


int main() {
    freopen("B.in.txt","r",stdin);
    freopen("B.out.txt","w",stdout);
    auto t00 = std::chrono::system_clock::now();
    //solveAll(10);
    //testAll(10);
    int nt;
    cin >> nt;
    vector<Solver> s(nt);
    for (int it = 0; it < nt; ++it) {
        s[it].read(cin);
    }
    const int np = 5;
    atomic<int> next(0);
    auto work = [&next, &s, &nt, t00](void) {
        while (true) {
            int i = next++;
            if (i >= nt)
                return;
            auto t0 = now();
            s[i].solve();
            double t = since(t0);
            if (t > 0.01)
                fprintf(stderr, "%3d : %3d / %d = %.2f | %.2f\n", i + 1, int(next) + 1, nt, t,
                        since(t00) / (int(next) + 1) * nt);
        }
    };
    vector<thread> workers;
    for (int i = 0; i < np; ++i) {
        workers.pb(thread(work));
    }
    for (int i = 0; i < np; ++i) {
        workers[i].join();
    }

    for (int it = 0; it < nt; ++it) {
        cout << "Case #" << (it + 1) << ": " << s[it].str() << endl;
    }
    fprintf(stderr, "%.2f\n", since(t00));
    return 0;
}

