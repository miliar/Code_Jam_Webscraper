#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int n,tt,vis[1100000];
double d[1100000];
//short nex[1100000][22];
inline int ask(const int &msk, const int &i)
{
    int j=i;
    while(!((msk>>j)&1))
    {
        j++;
        if(j==n)    j=0;
    }
    return j;
}
double dp(int msk)
{
    if(vis[msk]==tt)    return d[msk];
    vis[msk]=tt;
    if(msk==0)  return d[msk]=0.0;
    double res=0;
    for(int i=0;i<n;++i)
    {
        int j=i,k=0;
        while(!((msk>>j)&1))
        {
            j++;
            k++;
            if(j==n)    j=0;
        }
        res+=(n-k+dp(msk^(1<<j)));
    }
    return d[msk]=(res+0.0)/(n+0.0);
}
char s[22];
int main()
{
    freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);

    int tes;
    scanf("%d",&tes);
    for(tt=1;tt<=tes;++tt)
    {
        scanf("%s",s);
        n=strlen(s);
        int msk=0;
        for(int i=0;i<n;++i)if(s[i]=='.')
            msk|=(1<<i);
        printf("Case #%d: %.12lf\n",tt,dp(msk));
    }
    return 0;
}
