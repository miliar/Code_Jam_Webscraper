#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>
#include <bitset>
using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<pair<LL,LL> > VPLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-11
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORR(i, a, b) for (int i = (int) (a); i <= (int) (b); ++i)
#define FORE(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SIZE(x) ((int) ((x).size()))

#define PB push_back
#define MP make_pair

vector<int> bases = {2, 3, 4, 5, 6, 7, 8, 9, 10};


template <size_t N>
ULL interpret_in_base(bitset<N> n, int base){
    ULL res = 0;
    FORD (i, n.size()) {
        res *= base;
        res += n[i];
    }
    cerr << res << endl;
    return res;
}


template <size_t N>
int get_divisor_for_base(bitset<N> n, int base) {
    ULL cn = interpret_in_base(n, base);
    ULL m = ceil(sqrt(cn));
    for(auto i = 2; i <= m; i++) {
        if (cn % i == 0) {
            return i;
        }
    }
    return 0;
}


template <size_t N>
vector<int> test(bitset<N> n){
    cerr << ":" << n << endl;
    vector<int> divisors;
    for(auto base: bases) {
        auto divisor = get_divisor_for_base(n, base);
        if (divisor) {
            divisors.PB(divisor);
        } else {
            return vector<int>();
        }
    }
    return divisors;
}

int main(){
    // int t;
    // cin >> t;
    // int n, j;
    // cin >> n >> j;

    const ULL n = 16;
    int j = 50;

    cout << "Case #1:" << endl;

    ULL start = (1L << n - 1) + 1;
    ULL end = (1L << n) - 1;
    for (ULL i = start; i<= end; i+=2) {
        // if (i % 1000 == 0) cerr << i-start << endl;
        bitset<n> jamcoin(i);
        vector<int> divisors = test(jamcoin);
        if (divisors.size() == bases.size()) {
            cout << jamcoin;
            for (auto d: divisors) {
                cout << " " << d;
            }
            cout << endl;
            j--;
        }
        if (!j) {
            break;
        }
    }
    return 0;
}

