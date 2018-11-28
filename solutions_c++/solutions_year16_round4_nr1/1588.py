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
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <fstream>
#include <future>
#include <thread>
#include <chrono>
#include <iomanip>
#include <numeric>
#include <thread>
#include <atomic>
#include <random>

using namespace std;
typedef int64_t int64;
#define be(coll) std::begin(coll), std::end(coll)

template<typename T, typename U>
bool contains(T &&c, U &&x) {
    return find(std::begin(c), std::end(c), x) != std::end(c);
}

class MaxFlow {
public:
    struct Edge {
        int v1;
        int v2;
        int reverse;
        int64 capacity = 0;
        int64 flow = 0;
    };
    vector<Edge> edges;
    vector<vector<int>> graph;

    MaxFlow(int n) : graph(n) {}

    void addEdge(int a, int b, int64 capacity) {
        Edge e, r;
        e.v1 = r.v2 = a;
        e.v2 = r.v1 = b;
        e.capacity = capacity;
        e.reverse = int(edges.size() + 1);
        r.reverse = int(edges.size());
        graph[e.v1].push_back(int(edges.size()));
        edges.push_back(e);

        graph[r.v1].push_back(int(edges.size()));
        edges.push_back(r);
    }

    // Edmonds Karp
    int64 maxFlow(int s, int t) {
        int64 flow = 0;
        for (auto & e : edges)
            e.flow = 0;
        for (;;) {
            vector<int> curGen(1, s);
            vector<int> nextGen;
            vector<int> precedingEdge(graph.size(), -1);
            vector<int> terminalEdge;
            while (!curGen.empty()) {
                for (auto cur : curGen) {
                    for (auto ei : graph[cur]) {
                        Edge const & e = edges[ei];
                        if (precedingEdge[e.v2] < 0 && e.v2 != s && e.capacity > e.flow) {
                            if (e.v2 == t) {
                                terminalEdge.push_back(ei);
                            }
                            else {
                                precedingEdge[e.v2] = ei;
                                nextGen.push_back(e.v2);
                            }
                        }
                    }
                }
                swap(curGen, nextGen);
                nextGen.clear();
            }
            if (terminalEdge.empty())
                break;

            for (auto tei : terminalEdge) {
                int64 df = numeric_limits<int64>::max();
                for (int ei = tei; ei >= 0; ei = precedingEdge[edges[ei].v1]) {
                    df = min(df, edges[ei].capacity - edges[ei].flow);
                }

                for (int ei = tei; ei >= 0; ei = precedingEdge[edges[ei].v1]) {
                    edges[ei].flow += df;
                    edges[edges[ei].reverse].flow -= df;
                }

                flow += df;
            }
        }
        return flow;
    }

    // bipartitate minCoverage with s and t as added source/sink nodes
    int minCoverage(int s, int t) {
        maxFlow(s, t);
        vector<bool> covered(graph.size(), false);
        int ne = 0;
        for (auto const & e : edges) {
            if (e.flow > 0 && e.v1 != s && e.v2 != t) {
                covered[e.v1] = true;
                covered[e.v2] = true;
                ne++;
            }
        }
        ne += int(std::count(be(covered), false));
        return ne - 2;
    }
};

// functional form of next value in a stream
template<typename T>
T nextValue(std::istream &in) {
    T i;
    in >> i;
    return i;
}

// reads a vector (of integral values) from an input stream
template<typename T>
std::vector<T> readVector(std::istream &in, int n) {
    std::vector<T> c;
    std::generate_n(std::back_inserter(c), n, [&in]() { return nextValue<T>(in); });
    return c;
}

std::chrono::time_point<std::chrono::system_clock> now() { return std::chrono::system_clock::now(); }

double since(const std::chrono::time_point<std::chrono::system_clock> &t0) {
    return std::chrono::duration<double>(std::chrono::system_clock::now() - t0).count();
}

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

static int64 lcm(int64 a, int64 b) {
    if (a < 0 || b < 0)
        return -1;  // bad input
    if (a == 0 || b == 0)
        return 0;
    int64 k = a / gcd(a, b) * b;
    if (k < 0 || a < 0 || b < 0 || k % a != 0 || k % b != 0)
        k = -1;  // overflow
    return k;
}


// An iterator that represents a int with a fixed increment (defaulting to 1).
class CountingIterator : public std::iterator<std::random_access_iterator_tag, int> {
    int pos;
    int inc;
public:
    CountingIterator(int first, int inc_ = 1) : pos(first), inc(inc_) {}

    int& operator*() { return pos; }

    //int const * operator->() const { return &pos; }
    int operator[](int i) const { return pos + i * inc; }

    CountingIterator& operator++() { pos += inc; return *this; }
    CountingIterator& operator--() { pos -= inc; return *this; }

    CountingIterator& operator +=(int i) { pos += i * inc; return *this; }
    CountingIterator operator +(int i) const { return CountingIterator(pos + i * inc, inc); }
    CountingIterator& operator -=(int i) { pos -= i * inc; return *this; }
    CountingIterator operator -(int i) const { return CountingIterator(pos - i * inc, inc); }

    friend bool operator==(CountingIterator a, CountingIterator b) { return a.pos == b.pos; }
    friend bool operator!=(CountingIterator a, CountingIterator b) { return a.pos != b.pos; }
    friend CountingIterator operator+(int i, CountingIterator const & right) { return CountingIterator(i * right.inc + right.pos); }
    friend CountingIterator operator-(int i, CountingIterator const & right) { return CountingIterator(i * right.inc - right.pos); }
};


// returns lowest number, n, for which f(n) >= value
// f must be non-decreasing
template<typename I, class T, typename Func>
I lower_bound_argument(I first, I last, const T& value, Func f) {
    I count = last - first;
    while (count > 0) {
        I i = first;
        I step = count / 2;
        i += step;
        if (f(i) < value) {
            first = ++i;
            count -= step + 1;
        }
        else
            count = step;
    }
    return first;
}

// returns lowest number, n, for which f(n) >= value
// f must be non-decreasing
template<typename I, class T, typename Func>
I upper_bound_argument(I first, I last, const T& value, Func f) {
    I count = last - first;

    while (count > 0) {
        I i = first;
        I step = count / 2;
        i += step;
        if (!(f(i) < value)) {
            first = ++i;
            count -= step + 1;
        }
        else
            count = step;
    }
    return first;
}

// base class: override with a specific problem
class SolverBase {
    std::ostringstream out_;
public:
    virtual void read(std::istream &in) = 0;    // read input for a single test case

    virtual void solve() { saw(out_); }     // solve a single test case

    virtual void write(std::ostream &out) { out << out_.str(); }    // write output (after "Case: #N: ")

    string str() { return out_.str(); }

    operator string() { return out_.str(); }

protected:
    virtual void saw(std::ostream &out) = 0;    // solve and write
};

class Solver : public SolverBase {
    int n_, r_, p_, s_;
public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);

    bool legal(int j, int np);
};


void Solver::read(std::istream &in) {
    in >> n_ >> r_ >> p_ >> s_;
}

static int64 pow(int64 a, int64 p) {
    int64 ap = a; // a^1
    int64 result = 1;
    while (p != 0) {
        if ((p & 1) == 1) {
            result *= ap;
        }
        ap *= ap;
        p = p / 2;
    }
    return result;
}


static int winner(int k, int np) {
    if (np == 1)
        return k;
    int na = int(pow(3, np / 2));
    int wa = winner(k / na, np / 2);
    int wb = winner(k % na, np / 2);
    if (wa < 0 || wb < 0 || wa == wb)
        return -1;
    switch (wa + wb) {
        case 1: return 0;   // p > r
        case 2: return 2;   // s > p
        case 3: return 1;   // r > s
        default: throw 1;
    }
}

void Solver::saw(std::ostream &out) {
    int np = 1 << n_;
    char text[] = "PRS";
    int nc = int(pow(3, np));
    for (int j = 0; j < nc; ++j) {
        if (legal(j, np) && winner(j, np) >= 0) {
            int x = nc / 3;
            for (int i = 0; i < np; ++i) {
                out << text[j / x];
                j = j % x;
                x /= 3;
            }
            return;
        }
    }
    out << "IMPOSSIBLE";

}

bool Solver::legal(int k, int np) {
    int c[3];
    c[0] = p_;
    c[1] = r_;
    c[2] = s_;
    int x = int(pow(3, np));
    for (int i = 0; i < np; ++i) {
        x /= 3;
        int a = k / x;
        if (c[a] == 0)
            return false;
        c[a] --;
        k = k % x;
    }
    assert(c[0] == 0 && c[1] == 0 && c[2] == 0);
    return true;
}


int main() {
    freopen("A.in.txt", "r", stdin);
    freopen("A.out.txt", "w", stdout);

    auto t00 = std::chrono::system_clock::now();

    int nTestCases ;
    cin >> nTestCases;

    // number of processors
    const int nThreads = min(max(int(thread::hardware_concurrency()), 8), nTestCases);

    if (nThreads <= 1) {
        // sequential processing: less memory and useful for debugging
        Solver s;
        for (int it = 0; it < nTestCases; ++it) {
            s.read(cin);
            s.solve();
            cout << "Case #" << (it + 1) << ": " << s.str() << endl;
        }
    }
    else {
        // parallel processing with simple thread pool
        vector<Solver> s(nTestCases);
        // read all input sequentially
        for (int it = 0; it < nTestCases; ++it) {
            s[it].read(cin);
        }

        atomic<int> next(0);    // the next case that needs a worker thread
        atomic<int> done(0);    // only used for progress reporting

        auto work = [&next, &done, &s, &nTestCases, t00](void) {
            while (true) {
                int i = next++; // this atomic operation is how the threads synchronize with each other
                if (i >= nTestCases)
                    return;
                //fprintf(stderr, "start %3d\n", i + 1);
                auto t0 = now();
                s[i].solve();
                double t = since(t0);
                done++;
                if (t > 0.01)
                    fprintf(stderr, "%3d : %3d / %d = %.2f | %.2f\n", i + 1, int(done), nTestCases, t,
                            since(t00) / done * nTestCases);
            }
        };
        vector<thread> workers;
        // start worker threads
        for (int i = 0; i < nThreads; ++i) {
            workers.push_back(thread(work));
        }
        // wait for all workers to complete
        for (int i = 0; i < nThreads; ++i) {
            workers[i].join();
        }
        // report results
        for (int it = 0; it < nTestCases; ++it) {
            cout << "Case #" << (it + 1) << ": " << s[it].str() << endl;
        }
    }
    fprintf(stderr, "%.2f\n", since(t00));
    return 0;
}