#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<vector>
#include<map>
//#include<set>
#include<stdlib.h>
#include<ctype.h>
#include<utility>
#include<cmath>
using namespace std;
//#define REP(k,x,y) for(k=x;k<y;k++)
#pragma comment(linker, "/STACK:1024000000,1024000000")
#define eps 1e-6
#define ll long long
#define i64 __int64
#define INF 2000000000
#define pb push_back
#define sz(b) (int)b.size()
#define lson k<<1
#define rson k<<1|1
#define MOD 10007
#define CLR(t,x) memset(t,x,sizeof(t));
#define N 1000005
#define ls ch[p][0]
#define rs ch[p][1]
#define rp ch[rt][1]
#define lrp ch[rp][0]
double a[15],b[15];
int del[15];
int main()
{
    freopen("E:\\D-small-attempt0.in","r",stdin);
    freopen("E:\\D-small-attempt0.out","w",stdout);
    int cas,n,tt=1;
    scanf("%d",&cas);
    while(cas--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%lf",&a[i]);
        for(int i=0;i<n;i++) scanf("%lf",&b[i]);
        sort(a,a+n);sort(b,b+n);
        int ans1=0;
        for(int k=0;k<n;k++)
        {
            int sum=0;
            for(int i=0;i<k;i++) if(a[i]>b[n-i-1]) sum++;
            for(int i=k;i<n;i++) if(a[i]>b[i-k]) sum++;
            if(sum>ans1) ans1=sum;
        }
        int ans2=0;
        CLR(del,0);
        for(int i=0;i<n;i++)
        {
            int ok=0;
            for(int j=0;j<n;j++)
                if(b[j]>a[i]&&!del[j]) {del[j]=1;ok=1;break;}
            if(!ok) ans2++;
        }
        printf("Case #%d: %d %d\n",tt++,ans1,ans2);
    }
    return 0;
}
