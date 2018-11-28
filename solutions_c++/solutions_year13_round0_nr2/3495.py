#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int map[105][105];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,Case=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;++i)
            for(int j=1;j<=m;++j)
            scanf("%d",&map[i][j]);
        int flag=1;
        for(int i=1;i<=n;++i)
            for(int j=1;j<=m;++j)
            {
                int u=1,d=1,l=1,r=1;
                for(int ii=0;ii<i;++ii)
                    if(map[ii][j]>map[i][j])u=0;
                for(int ii=i+1;ii<=n;++ii)
                    if(map[ii][j]>map[i][j])d=0;
                for(int ii=0;ii<j;++ii)
                    if(map[i][ii]>map[i][j])l=0;
                for(int ii=j+1;ii<=m;++ii)
                    if(map[i][ii]>map[i][j])r=0;
                if(u+d!=2&&l+r!=2)flag=0;
            }
        printf("Case #%d: ",++Case);
        if(flag)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
