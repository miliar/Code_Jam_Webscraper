#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#define FI first
#define SE second
using namespace std;
const double EPS = 1e-8;
const int MAXN = 1005;
const int BIG = 100000;
const int INF = 111111111;
int a[MAXN],b[MAXN];
bool via[BIG*20],vib[BIG*20];

int dele(int n,int &pre) {
    int ret = n;
    for (int i = n-1; i >= 0; --i) {
        if (a[i]>b[i]) {
            --ret;
            ++pre;
        }
        else break;
   }
   return ret;
}
int main()
{
    freopen("/home/qitaishui/practice/retired/in.txt","r",stdin);
    freopen("/home/qitaishui/practice/retired/out.txt","w",stdout);
    int cas;
    int n;
    double in;
    scanf("%d",&cas);
    for (int ca = 1;  ca <= cas; ++ca) {
        scanf("%d",&n);
        memset(vib,0,sizeof(vib));
        memset(via,0,sizeof(via));
        for (int i = 0; i < n; ++i) {
            scanf("%lf",&in);
            in *= BIG;
            a[i] = (int)in;
        }
        for (int i = 0; i < n; ++i) {
            scanf("%lf",&in);
            in *= BIG;
            b[i] = (int)in;
            vib[b[i]] = 1;
        }
        sort(a,a+n);
        sort(b,b+n);
        int war,cwar,pb,pre;
        pre = war = cwar = 0;
        pb = 0;
        for (int i = 0; i < n; ++i) {
            while (pb < n &&a[i] > b[pb]) {
                ++pb;
            }
            if (pb < n) ++war;
            ++pb;
        }
        war = n-war;
        pb = n-1;

        while(n) {
            n = dele(n,cwar);
            if (n) {
                a[0] = b[n-1] = INF;
                sort(a,a+n);
                sort(b,b+n);
                --n;
            }

        }
        printf("Case #%d: %d %d\n",ca,cwar,war);
    }
    return 0;
}
