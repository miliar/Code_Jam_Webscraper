#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>
#define forup(i,a,b) for (int i=a;i<=b;i++)
#define fordown(i,a,b) for (int i=a;i>=b;--i)

using namespace std;

int T,m,n,a[41],v[41];

int main(){
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    scanf("%d",&T);
    forup(uu,1,T)
    {
        scanf("%d%d",&m,&n);
        memset(v,0,sizeof(v));
        memset(a,0,sizeof(a));
        forup(i,1,n) scanf("%d",&a[i]);
        double ans=0;
        forup(i,1,m)
        {
             int pos=0,Min1=1<<30,Min2=1<<30;
             forup(j,1,37)
                if (a[j]<Min1 || (a[j]==Min1 && v[j]<Min2)) 
                     Min1=a[j],Min2=v[j],pos=j;
             ++v[pos];++a[pos];
             Min1=1<<30;
             forup(j,1,37) Min1=min(Min1,a[j]);
             int cnt=0;
             forup(j,1,37)
                   if (a[j]==Min1) ++cnt;
             double now=0;
             forup(j,1,37) 
                 if (Min1==a[j]) 
                     now+=1.0/(double)cnt*(double)36*(double)v[j];
             ans=max(ans,now-i);
        }
        printf("Case #%d: %.10lf\n",uu,ans);
    }
}
