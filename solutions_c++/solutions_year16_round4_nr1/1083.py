#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int a[4100];

bool solve(int p, int r, int s, int st, int en)
{
    //printf("%d %d %d %d %d\n",p,r,s,st,en);
    if(p%2==0&&r%2==0&&s%2==0) return false;
    if(st+1==en)
    {
        int i=st;
        if(p>1||r>1||s>1) return false;
        if(p==1) a[i]=0,i++;
        if(r==1) a[i]=1,i++;
        if(s==1) a[i]=2,i++;
        return true;
    }
    int lp,lr,ls,rp,rr,rs;
    if(p%2==0)
    {
        lp=rp=p/2;
        lr=ceil(r/2.0);
        rr=floor(r/2.0);
        ls=floor(s/2.0);
        rs=ceil(s/2.0);
    }
    else if(r%2==0)
    {
        lr=rr=r/2;
        lp=ceil(p/2.0);
        rp=floor(p/2.0);
        ls=floor(s/2.0);
        rs=ceil(s/2.0);
    }
    else if(s%2==0)
    {
        ls=rs=s/2;
        lp=ceil(p/2.0);
        rp=floor(p/2.0);
        lr=floor(r/2.0);
        rr=ceil(r/2.0);
    }
    int mid=(st+en)/2;
    if(!solve(lp,lr,ls,st,mid)) return false;
    if(!solve(rp,rr,rs,mid+1,en)) return false;
    return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int n,r,p,s;
    for(int cases=1;cases<=T;cases++)
    {
        scanf("%d%d%d%d",&n,&r,&p,&s);
        printf("Case #%d: ", cases);
        int len=1<<n;
        if(solve(p,r,s,0,len-1))
        {
            for(int i=0;i<len;i++)
            {
                if(a[i]==0) putchar('P');
                else if(a[i]==1) putchar('R');
                else if(a[i]==2) putchar('S');
            }
            puts("");
        }
        else
        {
            puts("IMPOSSIBLE");
        }
    }
    return 0;
}
