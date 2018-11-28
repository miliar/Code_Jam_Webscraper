#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int s[101][101];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        int m,n;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                scanf("%d",&s[i][j]);
        int cnt=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
            {
                if(s[i][j]==1)
                {
                    int cnt1=0,cnt2=0;
                    for(int ii=1;ii<=n;ii++)
                    {
                        if(s[ii][j]!=1)
                            cnt1=1;
                    }
                    for(int ii=1;ii<=m;ii++)
                    {
                        if(s[i][ii]!=1)
                            cnt2=1;
                    }
                    if(cnt1==1&&cnt2==1)
                        cnt=1;
                }
            }
        printf("Case #%d: ",cases);
        if(cnt)
            printf("NO\n");
        else
            printf("YES\n");
    }
    return 0;
}
