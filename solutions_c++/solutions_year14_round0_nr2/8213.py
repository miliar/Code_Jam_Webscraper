#include <cstdio>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <bitset>

#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

using namespace std;

typedef long long ll;
typedef unsigned long long llu;

double C, F, X;
int lim;
double R(int m){
    double A = F * m + 2;
    if ( m == lim ) return X / A;
    
    return min(X / A, R(m + 1) + C / A);
}

double res[200000];
double RR(int m){
    double A = F * lim + 2;
    res[lim] = X / A;
    for ( int i = lim-1 ; i >= 0 ; i-- ){
        A = F * i + 2;
        res[i] = min(X / A, res[i+1] + C/A);
    }
    
    return res[0];
}

int main(){
    int test, ks;
    
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    while ( scanf("%d", &test) == 1 ){
        for ( ks = 1 ; ks <= test ; ks++ ){
            scanf("%lf%lf%lf", &C, &F, &X);
            printf("Case #%d: ", ks);

            lim = 200000;
            printf("%.10lf\n", RR(0 ));
        }
    }
    
    return 0;
}
