#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <memory.h>

using namespace std;
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s); i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define EXP(i,l) for (int i=(l); i; i=qn[i])
#define LL long long
#define eps 1e-6
#define pi acos(-1.0)

LL max(LL a,LL b){if (a>b){return a;} else {return b;}}
LL min(LL a,LL b){if (a<b){return a;} else {return b;}}

struct P{
    double x, y;
    P(){}
    P(double x, double y):x(x) , y(y){}
    P operator+ (const P &a) const {return P(x+a.x, y+a.y);}
    P operator- (const P &a) const {return P(x-a.x, y-a.y);}
    double operator^ (const P &a) const {return x*a.x+y*a.y;}
    void in(){scanf("%lf%lf", &x, &y);}
    void out(){printf("REQUIRED %.7f %.7f\n", x, y);}
    double dist(P a, P b) {return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));}
    double sqdist(P a, P b) {return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y);}

};

int n;
int T, x;
int a[10001];
int v[10001];

void solve(int tc){
    printf("Case #%d: ", tc);
    scanf("%d%d", &n, &x);
    FOE(i, 1, n) scanf("%d", &a[i]);
    sort(a+1, a+n+1);
    int res = 0;
    FOE(i, 1, n) v[i] = 0;
    FOD(i, n, 1) if (v[i] == 0){
        v[i] = 1;
        res++;
        int P = -1;
        FOE(j, 1, n) if ((v[j] == 0) && (a[i] + a[j] <= x)) P = j;
        if (P != -1) v[P] = 1;
    }
    printf("%d\n", res);

}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &T);
    FOE(i, 1, T) solve(i);
    return 0;
}
