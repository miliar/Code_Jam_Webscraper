#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<map>

using namespace std;

const int MAX = 1200;
bool vis[MAX];

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int N;
    scanf("%d",&N);
    for(int i=1;i<=N;i++)
    {
        printf("Case #%d: ",i);
        double nic[MAX],nep[MAX];
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)scanf("%lf",nic+i);
        for(int i=0;i<n;i++)scanf("%lf",nep+i);
        int ans_d = 0,ans_w =0;
        sort(nic,nic+n);
        sort(nep,nep+n);
        bool nep_w_f;
        memset(vis,0,sizeof(vis));
        for(int i=0;i<n;i++)
        {
           nep_w_f = false;
           for(int j=0;j<n;j++)
             if( nic[j]>nep[i] && vis[j]==false)
             {
                nep_w_f=true;
                vis[j]=1;
                break;
             }
             if(nep_w_f==true)
                ans_d++;
       }
       memset(vis,0,sizeof(vis));
       for(int i=0;i<n;i++)
       {
          nep_w_f = false;
          for(int j=0;j<n;j++)
              if(vis[j]==false && nep[j]>nic[i])
              {
                 nep_w_f = true;
                 vis[j]=1;
                 break;
              }
          if(nep_w_f==false)
            ans_w++;
       }
       printf("%d %d\n",ans_d,ans_w);
    }
       return 0;
}

