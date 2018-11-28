#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <utility>

typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::pair<ll, ll> pll;

const int MAX = 222;
int N, K;
double P[MAX];

unsigned int next(unsigned int v) {
    unsigned int t = v | (v - 1);
    return (t + 1) | (((~t & -~t) - 1) >> (__builtin_ctz(v) + 1));
}

unsigned nChoosek( unsigned n, unsigned k )
{
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;    

    int result = n;
    for( int i = 2; i <= k; ++i ) {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}

double calc(const std::vector<double> & v) {
    int sz = v.size();
    double evts = nChoosek(sz, sz / 2);
    double res = 0.0;
    unsigned int msk = (1<<(sz/2)) - 1;
    while(msk < (1<<sz)) {
        double yes = 1.0;
        double no = 1.0;

        for(int i = 0; i < sz; ++i) {
            if(msk & (1<<i)) yes *= v[i];
            else             no *= (1 - v[i]);
        }

        res += (yes * no);
        msk = next(msk);
    }
    return res;
}

double brute() {
    unsigned int msk = (1<<K) - 1;
    double best = 0.0;
    while(msk < (1<<N)) {
        std::vector<double> hld;
        for(int i = 0; i < N; ++i)
            if(msk & (1<<i)) hld.push_back(P[i]);

        double here = calc(hld);
        if(here > best) {
            best = here;
        }
        msk = next(msk);
    }
   
    return best;
}

std::vector<double> greed;
double mem[222][111][111];
bool seen[222][111][111];

double rec(int pos, int yl, int nl) {
    if(pos == greed.size()) return (yl == 0) && (nl == 0);
    if(yl < 0) return 0.0;
    if(nl < 0) return 0.0;
    if(seen[pos][yl][nl]) 
        return mem[pos][yl][nl];
    seen[pos][yl][nl] = true;
    double voteY = rec(pos + 1, yl - 1, nl) * greed[pos];
    double voteN = rec(pos + 1, yl, nl - 1) * (1 - greed[pos]);

    return mem[pos][yl][nl] = voteN + voteY;
}

double solve() {
    double best = 0.0;
    for(int i = 0; i <= K; ++i) {
        greed.clear();
        for(int j = 0; j < i; ++j) greed.push_back(P[j]);
        for(int j = 0; j < K - i; ++j) 
            greed.push_back(P[N - j - 1]);

        memset(seen, false, sizeof(seen));
        double here = rec(0, K / 2, K / 2);
        best = std::max(here, best);
    }
    return best;
}

int main() {
    int CS;
    std::cin >> CS;
    std::cout << std::fixed << std::setprecision(8);
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N >> K;
        for(int n = 0; n < N; ++n)
            std::cin >> P[n];
        std::sort(P, P + N);

        // double ans = brute();
        double ans = solve();
        std::cout << "Case #" << cs << ": " << ans << std::endl;
    }
}
