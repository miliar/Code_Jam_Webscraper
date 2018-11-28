#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define inf 1<<30
#define Mod 10000007
#define dbg(a) printf("%d\n",a);
#define sz(a) (a).size()
int n,m;int a[10002],cnt[10002],maxx[10002];
int MX;


int main()
{
    int i,j,k,T,cs=0;int ans,n;
    freopen("B-large.in","r",stdin);
    //freopen("B-small-attempt1.in","r",stdin);
    freopen("bout.txt","w",stdout);


    cin>>T;

    while(T--)
    {
        scanf("%d",&n);
        ans=20000;MX=-1;
        for(i=1;i<=n;i++)
        {
            cin>>a[i];

            MX=max(MX,a[i]);
        }

       for(i=1;i<=MX;i++)
       {
          int tmp=0;
          for(j=1;j<=n;j++)
          {
              if(a[j]>i)tmp=tmp+(a[j]+i-1)/i-1;
          }
          ans=min(ans,tmp+i);
          //printf("%d %d\n",i,tmp);
       }
        printf("Case #%d: %d\n",++cs,ans);

    }

    return 0;
}

