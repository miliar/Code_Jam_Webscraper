#include <cstdio>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <bitset>
#include <iostream>
using namespace std;
typedef long long ll;
typedef double db;
const int maxn = 1005;

int n,a[maxn];

int main() {
    //freopen("in.cpp", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int T,ncase=0;
    scanf("%d",&T);
    while(T--) {
        scanf("%d",&n);
        int ret=0,mx=0;
        for(int i=1; i<=n; i++) {
            scanf("%d",&a[i]);
            mx=max(mx,a[i]);
        }
        ret=mx;
        for(int i=1; i<=mx; i++) {
            int cnt=0;
            for(int j=1; j<=n; j++)
                if(a[j]>i)cnt+=(a[j]-1)/i;
            ret=min(ret,cnt+i);
        }
        printf("Case #%d: %d\n",++ncase,ret);
    }
    return 0;
}
