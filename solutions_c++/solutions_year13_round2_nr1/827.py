/*BRUM BRUM BRUM*/

// input/output
#include <cstdio>
#include <iostream>
// structures
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <tuple>
// other stuff
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <utility>

using namespace std;

#define dbg if(0)
#ifdef EBUG 
    #define dbg if(1) 
#endif
#define db(x) dbg cerr << #x << "\t: " << (x) <<  endl;
#define dbv(x) dbg{ cerr << #x << "\t: "; FOREACH(it, x) cerr << *it << " "; cerr << endl;}

// vlastny assert
#define EXIT 0
#define WA 3
#define TLE 1
#define EXC 2
#define assert(x, ...) if(!(x)){ cerr << "F: " << __FUNCTION__ << "(), L: " << __LINE__ << ", (" << #x << ") isn\'t true\n"; error_exit(__VA_ARGS__); }
void error_exit(int error=EXIT){
    switch(error){
        case EXIT:   exit(0);                    break;
        case WA:     cout << "BRUM BRUM BRUM\n"; break;
        case TLE:    while(47){};                break;
        case EXC:    int *q47; q47[1000047] = 47;break;
    }
}

#define MINIM(x, y) x = min(x, (y))
#define MAXIM(x, y) x = max(x, (y))
#define iter(x) typeof((x).begin())
#define FOR(i,n) for(long long i = 0; i < (n); ++i)
#define FOR1(i, n) for(long long i = 1; i <= (n); ++i)
#define FOREACH(it, str) for(typeof((str).begin()) it = (str).begin(); it != (str).end(); ++it)
#define mp make_pair
#define mt make_tuple
#define pf printf
#define sf scanf
#define PASS
typedef long long ll;
const long long INF = 2000000000;
const double EPS = 1e-9;
typedef pair<long long, long long> pll;
typedef pair<int,int> pii;

int main(){
    int T;
    sf(" %i", &T);
    FOR1(tt,T){
    	ll A, N;
    	sf(" %lli %lli", &A, &N);
    	db(A); db(N); 
        vector<ll> a(N);
        FOR(i, N) sf(" %lli", &a[i]);
        sort(a.begin(), a.end());

        ll best_res = INF;
        ll pridane = 0;
        ll pos = 0;
        while (pos < N && pridane <= N){
            if(A > a[pos]){
                A += a[pos];
                ++pos;
            }
            else{
                MINIM(best_res, pridane + N-pos); // keby som tu skoncil
                while(A <= a[pos] && pridane <= N){ A += A-1; ++pridane;}
            }
        }
        MINIM(best_res, pridane);
        pf("Case #%lli: %lli\n", tt, best_res);
    }
}
