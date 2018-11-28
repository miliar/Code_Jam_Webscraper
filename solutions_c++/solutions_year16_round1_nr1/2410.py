

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
double since(const std::chrono::time_point<std::chrono::system_clock> &t0) {
    return std::chrono::duration<double>(std::chrono::system_clock::now() - t0).count(); }

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
    string s_;
public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);

};


void Solver::read(std::istream &in) {
    in >> s_;
}

void Solver::saw(std::ostream &out) {
    vector<char> result(s_.length() * 2 + 2);
    int b = int(s_.length());
    int e = b;
    for (auto c : s_) {
        if (b == e)
            result[e++] = c;
        else if (c >= result[b])
            result[--b] = c;
        else
            result[e++] = c;
    }
    for (int i = b; i < e; i++)
        out << result[i];
}



int main() {
    freopen("A.in.txt","r",stdin);
    freopen("A.out.txt","w",stdout);
    auto t00 = std::chrono::system_clock::now();
    int nt;
    cin >> nt;
    vector<Solver> s(nt);
    for (int it = 0; it < nt; ++it) {
        s[it].read(cin);
    }
    const int np = 7;
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
