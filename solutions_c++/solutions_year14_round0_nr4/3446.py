#include<cstring>
#include<fstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cctype>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
#include<ctime>
#include<cstdlib>
using namespace std;
#define PI acos(-1.0)
#define MAXN 1005
#define eps 1e-9
#define INF 0x7FFFFFFF

double a[MAXN];
double b[MAXN];
int c[MAXN],d[MAXN];
int main() {
    freopen ("D-large.in", "r", stdin);
    freopen ("D-large.out", "w", stdout);
    int t,kk=1;
    scanf("%d",&t);
    while(t--) {
        int tt;
        scanf("%d",&tt);
        for(int i=1; i<=tt; i++) {
            scanf("%lf",&a[i]);
            c[i]=(a[i]*100000+eps);
        }
        for(int i=1; i<=tt; i++) {
            scanf("%lf",&b[i]);
            d[i]=(b[i]*100000+eps);
        }
        sort(c+1,c+tt+1);
        sort(d+1,d+tt+1);
        int a1=1,b1=1;
        int an1=0,an2=0;
        while(a1<=tt) {
            if(c[a1]>d[b1]) {
                an1++;
                a1++;
                b1++;
            } else a1++;
        }
        a1=1,b1=1;
        while(b1<=tt) {
            if(d[b1]>c[a1]) {
                an2++;
                a1++;
                b1++;
            } else b1++;
        }
        printf("Case #%d: %d %d\n",kk++,an1,tt-an2);
    }
    return 0;
}
