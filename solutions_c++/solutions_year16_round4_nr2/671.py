#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <iomanip>

using namespace std;

#define pb push_back
#define f first
#define s second
typedef long long ll;
typedef pair<int, int> pint;
typedef pair<long long, long long> plint;
typedef vector<int> vint;
typedef vector<vector<int>> vvint;
typedef vector<long long> vlint;
typedef vector<vector<long long>> vvlint;
typedef vector<pair<int, int>> vpint;
typedef vector<pair<long long, long long>> vplint;

ifstream in("B-small-attempt0.in");
ofstream out("output.txt");

class Stats {
public:
    Stats(int k_) : k(k_), p(0), prefix_stats(k), best(0) {
        for (int i = 0; i < k; ++i) {
            prefix_stats[i].resize(std::min(k / 2, i + 1) + 1);
        }
    }
    void push(double x) {
        PrefixStat &stat = prefix_stats[p];
        if (p == 0) {
            stat[0] = 1 - x;
            stat[1] = x;
            ++p;
            return;
        }
        const PrefixStat &pstat = prefix_stats[p - 1];
        for (int i = 0; i <= std::min(k / 2, p + 1); ++i) {
            stat[i] = x * (i > 0 ? pstat[i - 1] : 0) + (1 - x) * (i <= p ? pstat[i] : 0);
        }
        ++p;
        if (p == k) {
            best = std::max(best, stat[k / 2]);
        }
    }
    void pop() {
        --p;
    }
    double get_best() const {
        return best;
    }

private:
    int k;
    int p;
    double best;
    using PrefixStat = vector<double>;
    vector<PrefixStat> prefix_stats;
};


void go(int n, int k, const vector<double> &probs, int i, int got, Stats &stats)
{
    if (got == k) {
        return;
    }
    if (n - i < k - got) {
        return;
    }
    //cerr << i << " " << got << endl;
    stats.push(probs[i]);
    //cerr << stats.get_best() << endl;
    go(n, k, probs, i + 1, got + 1, stats);
    stats.pop();
    go(n, k, probs, i + 1, got, stats);
}


void solve()
{
    int n, k;
    in >> n >> k;
    vector<double> probs(n);
    for (double &x : probs) {
        in >> x;
    }

    Stats stats(k);
    go(n, k, probs, 0, 0, stats);
    out.precision(12);
    out << stats.get_best();
}

int main()
{
    int cases;
    in >> cases;
    for (int z = 0; z < cases; ++z) {
        out << "Case #" << z + 1 << ": ";
        solve();
        out << endl;
    }

    return 0;
}
