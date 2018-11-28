#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<set>
#include<map>
using namespace std;
int t;
int cap,n;
int a[101000];
int visit[100100];
int main(){

//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&n,&cap);
        printf("Case #%d: ",cas);
        for(int i=0;i<n;++i)
        {
            scanf("%d",&a[i]);
        }
        sort(a,a+n);
        memset(visit,0,sizeof(visit));
        int e=n-1,ans=0;
        for(int i=0;i<n;++i)
        {
            if(visit[i])continue;
            if(i<e&&a[i]+a[e]<=cap)
            {
                visit[i]=visit[e]=1;
                e--;
                ans++;
            }
            else
            {
                ans++;
            }
        }
        printf("%d\n",ans);
    }

    return 0;
}
