#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <iostream>
#include <complex>
#include <sstream>
using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
#define ALL(v) (v).begin(), (v).end()
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second


long double SN[100000];
void scase() {    
    int N,X,Y;
    scanf("%d%d%d",&N,&X,&Y);
    X = abs(X);

    if (X % 2 != Y % 2) {
        printf("%0.10lf\n", 0.0);
        return;
    }

    int K = 1;
    while ((K + 2) * (K + 3) / 2 <= N) K += 2;
    N -= K * (K + 1) / 2;

    int X0 = X + Y;
    if (X0 <= K - 1) {
        printf("%0.10lf\n", 1.0);
        return;
    } else if (X0 > K + 1 || X == 0 || Y > N) {
        printf("%0.10lf\n", 0.0);
        return;
    }
    
    long double result = 0;
    
    long double tmp = 1.0;
    REP(i,N+1) {
        int W = N - min(i,K+1);
        if (W >= Y + 1) result += tmp;
        tmp *= (N - i) * 1.0 / (i + 1);  

    }
    
    REP(i,N) result /= 2.0;

    printf("%0.10Lf\n", result);
       
}

int main() {
    int C;
    scanf("%d",&C);
    FOR(i,1,C+1) {
        printf("Case #%d: ", i);
        scase();
    }
}  
