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

int test;
char s1[21];
double f[1100001],way[1100001];

int main(){
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&test);
    forup(uu,1,test)
    {
         scanf("%s",s1);
         int n=strlen(s1),now=0;
         int cnt=0;
         forup(i,0,n-1)
            if (s1[i]=='X') now|=1<<i;
            else ++cnt;
         memset(f,0,sizeof(f));
         memset(way,0,sizeof(way));
         way[now]=1;
         forup(i,now,(1<<n)-2)
         if (way[i])
         {
               int need=n,empty=0;
               forup(k,0,n-1)
               if (!(i&(1<<k))) 
               {
                   need=n-k-1;
                   empty=k;
                   break;
               }
               fordown(k,n-1,0)
               {
                   if (!(i&(1<<k))) need=n,empty=k;
                   f[i|(1<<empty)]+=f[i]+way[i]*need;
                   way[i|(1<<empty)]+=way[i];
                   --need;
               }
         }
         double ans=0;
         ans=f[(1<<n)-1]/way[(1<<n)-1];
         printf("Case #%d: %.10lf\n",uu,ans);
    }
}
                       
