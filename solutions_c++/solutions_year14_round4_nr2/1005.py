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
int T;
int a[10001];
int pos[1001];
int lar;

struct edge{
    int po, w;
};


edge b[1001];

bool operator< (edge u, edge v) {return u.w < v.w;}

void solve(int tc){
    printf("Case #%d: ", tc);
    scanf("%d", &n);
    FOE(i, 1, n) scanf("%d", &a[i]);
    FOE(i, 1, n) {
        b[i].po = i;
        b[i].w = a[i];
    }
    sort(b+1, b+n+1);
    FOE(i, 1, n) pos[i] = b[i].po, a[pos[i]] = i;;
    int l = 1, r = n;
    int res = 0;
       // FOE(j, 1, n) printf("%d ", a[j]);
       // puts("");
    FOE(i, 1, n-1){
        //printf("%d\n", pos[i]);
        if (pos[i] - l < r - pos[i]){
            FOD(j, pos[i]-1, l){
                int t = a[j];
                a[j] = a[j+1];
                a[j+1] = t;
                pos[a[j]] = j;
                pos[a[j+1]] = j+1;
                res++;
            }
            l++;
        } else {

            FOE(j, pos[i], r-1){
                int t = a[j];
                a[j] = a[j+1];
                a[j+1] = t;
                pos[a[j]] = j;
                pos[a[j+1]] = j+1;
                res++;
            }
            r--;

        }
      //  FOE(j, 1, n) printf("%d ", a[j]);
      //  puts("");

    }
    printf("%d\n", res);

}
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &T);
    FOE(i, 1, T) solve(i);
    return 0;
}
