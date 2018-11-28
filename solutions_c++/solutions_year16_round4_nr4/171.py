#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<iomanip>
#include<algorithm>
using namespace std;
char s[705];
int p[35],used[35];
bool dfs(int d,int n,int mask)
{
    if(d==n)return 1;
    bool isok=1,work=0;
    for(int i=0;i<n;i++)
        if(!used[i] && (mask&(1<<p[d]*n+i)))
        {
            work=1;
            used[i]=1;
            isok&=dfs(d+1,n,mask);
            used[i]=0;
        }
    return isok&work;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%s",s+i*n);
            p[i]=i;
        }
        int res=n*n;
        for(int mask=0;mask<(1<<n*n);mask++)
        {
            bool isok=1;
            for(int i=0;i<n*n;i++)
                if((~mask&(1<<i)) && s[i]=='1')isok=0;
            if(!isok)continue;
            int cost=0;
            for(int i=0;i<n*n;i++)
                if((mask&(1<<i)) && s[i]=='0')cost++;
            isok=1;
            do{isok&=dfs(0,n,mask);}while(next_permutation(p,p+n));
            if(isok)res=min(res,cost);
        }
        printf("Case #%d: %d\n",ca,res);
    }
    return 0;
}
