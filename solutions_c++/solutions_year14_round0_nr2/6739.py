#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define dbg(x) cout << #x << " = " << x << endl
#define dbg2(x,y) cout << #x << " = " << x << ", " << #y << " = " << y << endl
#define rep(i,x,y) for(int i = (x); i < (y); i ++)
#define rep2(i,x,y) for(int i = (x); i <= (y); i ++)
#define dec(i,x,y) for(int i = (x); i >= (y); i --)
#define i64d long long

using namespace std;

double C, F, X;

double gao()
{
    double t_k = 0.0, k = 2.0, res = X / 2.0;
    while( t_k + 1e-9 < res ) {
        if( t_k + X / k + 1e-9 < res )
            res = t_k + X / k;
        t_k += C / k; k += F;
    }
    return res;
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int nt, idx = 0; scanf("%d", &nt);
    while( (nt --) > 0 ) {
        scanf("%lf %lf %lf", &C, &F, &X);
        printf("Case #%d: %.9lf\n", ++idx, gao());
    }
    return 0;
}
