// Dark Side of Elephant
// Askar

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <cstring>
#include <algorithm>
#include <utility>
#include <tuple>
#include <complex>
#include <cmath>

using namespace std;

#define FOR(i, N) for(auto i=(N)-(N); i<(N); ++i)
#define FOR1(i, N) for(auto i=(N)-(N)+1; i<=(N); ++i)
#define FOREACH(it, a) for(auto it=(a).begin(); it!=(a).end(); ++it)
#define MAXIM(a,b) a=max(a, static_cast<__typeof__(a)>(b))
#define MINIM(a,b) a=min(a, static_cast<__typeof__(a)>(b))
#define beginend(a) (a).begin(), (a).end()
#define pf printf
#define sf scanf
#define mp make_pair
#define mt make_tuple
#define pass
#define sqr(x) (x)*(x)
typedef long long ll;
typedef pair<long long, long long> pll;
typedef pair<int, int> pii;
const long long INF = 1e9;
const double EPS = 1e-9;

#define dbg if(false)
#ifdef EBUG
    #undef dbg
    #define dbg if(true)
#endif

#define epf(...) fprintf(stderr, __VA_ARGS__)
#define dpf(...) dbg epf(__VA_ARGS__)
#define db(x) dbg cerr << #x << ":\t" << (x) << endl 
#define assert(x, ...) if(!(x)){                                \
epf("L: %i, F: %s: (%s) failed!\n", __LINE__, __FUNCTION__, #x);\
error_exit(__VA_ARGS__);                                        \
}
const int WA = 0;
const int EXC = 1;
const int TLE = 2;
void error_exit(const int exit_type=WA){
    switch(exit_type){
        case WA: epf("\nWe want WA!\n"); exit(0); break; 
        case EXC: exit(47); break;
        case TLE: while(true); break;
    }
}

double fracsum(int n, double F){
    double res = 0;
    for(int k = n; k >= 0; k--){
        res += 1 / (2 + k*F);
    }

    return res;
}

int main(){
    int T;
    sf(" %i", &T);

    for(int t = 1; t <= T; t++){
        double C, F, X;
        sf(" %lf %lf %lf", &C, &F, &X);
        
        double bestres = X / 2;

        for(int n = 1;; n++){
            double preparing = C * fracsum(n-1, F);
            if(preparing > bestres) break;

            double res = preparing + X / (2 + n*F);

            MINIM(bestres, res);
        }
        pf("Case #%i: %.7lf\n", t, bestres);
    }

    dbg{
        double F = 100.0;
        for(int i = 0; i < 10000; i++){
            cerr << i << ":\t" << fracsum(i+1, F) << "\tdiff: " <<   fracsum(i+1, F) - fracsum(i, F) << endl;
        }
    }

}
