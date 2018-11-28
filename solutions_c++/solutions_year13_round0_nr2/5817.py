#include <iostream>
using namespace std;
#include <stdio.h>
int MAX(int a,int b) { return a>b?a:b; }
#include <algorithm>
#include <cstring>
int main()
{
   freopen("B-small-attempt1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,N,M;
    int FINAL[105][105];
    bool l[105];
    scanf("%d",&T);
    int cnt = 1;
    while(T--)
    {
        scanf("%d%d",&N,&M);
        for(int i=0;i<N;i++)
            for(int j=0;j<M;j++) scanf("%d",&FINAL[i][j]);
        memset(l,false,sizeof(l));
        for(int i=0;i<N;i++)
        {
            int j,cmp = FINAL[i][0];
            for(j=0;j<M;j++)
                if(cmp!=FINAL[i][j]) break;
            if(j==M) l[i] = true;
        }
        bool flag = true;
        for(int j=0;j<M&&flag == true;j++)
        {
            int i,cmp = FINAL[0][j];
            for(i=0;i<N;i++) cmp = MAX(cmp,FINAL[i][j]);
            for(i=0;i<N;i++)
            {
                if(l[i]==true) continue;
                if(cmp!=FINAL[i][j]) { flag = false; break; }
            }
        }
        if(flag) printf("Case #%d: YES\n",cnt++);
        else printf("Case #%d: NO\n",cnt++);
    }
}
