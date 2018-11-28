

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

class Solver : public SolverBase {
    int n_;
    vector<vector<int>> a_;
public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);

    bool place(vector<vector<int>> rc[2], int next);

    bool matches(int a, int b);
};


void Solver::read(std::istream &in) {
    in >> n_;
    for (int i = 0; i < 2 * n_ - 1; ++i) {
        a_.push_back(readVector<int>(in, n_));
    }
    /*
    string s;
    getline(in >> std::ws, s);
    for (auto c : s) {
        a_.push_back(c);
    }
     */
}

void Solver::saw(std::ostream &out) {
    vector<int> b(n_);
    int missing = -1;
    int offset = 0;
    vector<vector<int>> rc[2];
    rc[0].resize(n_);
    rc[1].resize(n_);
    for (int pos = 0; pos < n_; ++pos) {
        sort(a_.begin() + offset, a_.end(), [pos](vector<int> const & a, vector<int> const & b) { return a[pos] < b[pos]; });
        if (offset + 1 < a_.size() && a_[offset][pos] == a_[offset + 1][pos]) {
            rc[0][pos] = a_[offset];
            rc[1][pos] = a_[offset + 1];
            offset += 2;
        }
        else {
            rc[0][pos] = a_[offset];
            rc[1][pos].resize(n_, 0);
            missing = pos;
            offset += 1;
        }
    }
    place(rc, 1);
    int mside = rc[0][missing][0] == 0 ? 0 : 1;
    for (int j = 0; j < n_; ++j) {
        b[j] = rc[1 - mside][j][missing];
    }

    //b = a_[0];
    out << b[0];
    for (int i = 1; i < n_; ++i) {
        out << " " << b[i];
    }
}

bool Solver::place(vector<vector<int>> *rc, int next) {
    for (int side = 0; side < 2; ++side) {
        bool ok = true;
        for (int i = 0; i < next; ++i) {
            if (!matches(rc[0][next][i], rc[1][i][next]) || !matches(rc[1][next][i], rc[0][i][next])) {
                ok = false;
                break;
            }
        }
        if (ok && next + 1 < n_) {
            ok = place(rc, next + 1);
        }
        if (ok)
            return true;
        swap(rc[0][next], rc[1][next]);
    }
    return false;
}

bool Solver::matches(int a, int b) {
    return a == 0 || b == 0 || a == b;
}


int main() {
    freopen("B.in.txt","r",stdin);
    freopen("B.out.txt","w",stdout);
    auto t00 = std::chrono::system_clock::now();
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

