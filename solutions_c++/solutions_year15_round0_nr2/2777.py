//author: CHC
//First Edit Time:	2015-04-11 13:56
//Last Edit Time:	2015-04-11 13:56
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <limits>
using namespace std;
typedef long long LL;
const int MAXN=1e+4;
const int MAXM=1e+5;
const int INF = numeric_limits<int>::max();
const LL LL_INF= numeric_limits<LL>::max();
int a[MAXN];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,cas=0,n;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        int mm=0;
        for(int i=1;i<=n;i++){
            scanf("%d",&a[i]);
            mm=max(mm,a[i]);
        }
        int t,ans=INF;
        for(int i=1;i<=mm;i++){
            t=0;
            for(int j=1;j<=n;j++){
                if(a[j]>i){
                    if(a[j]%i==0) t+=a[j]/i-1;
                    else t+=a[j]/i;
                }
            }
            //printf("%d %d\n",i,t);
            ans=min(ans,i+t);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
