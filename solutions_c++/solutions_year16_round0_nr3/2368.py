#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int n,j,T,p[]={2,3,5,7,11,13,17,19,23,29};
vector<int>ans;
LL mul(LL a,LL b,LL mod)
{
    a%=mod;b%=mod;
    LL ans=0;
    while(b)
    {
        if(b&1)
        {
            ans+=a;
            if(ans>=mod)
                ans-=mod;
        }
        a<<=1;
        if(a>=mod)
            a-=mod;
        b>>=1;
    }
    return ans;
}
LL pow_mod(LL a,LL n,LL mod)
{
    LL ans=1;
    a%=mod;
    while(n)
    {
        if(n&1)
            ans=mul(ans,a,mod);
        a=mul(a,a,mod);
        n>>=1;
    }
    return ans;
}
bool check(LL x,int a,LL t,int cnt)
{
    if(a>=x)return 0;
    LL cur,last;
    last=pow_mod(a,t,x);
    while(cnt--)
    {
        cur=mul(last,last,x);
        if(cur==1)
        {
            if(last!=1&&last!=x-1)
                return 1;
            return 0;
        }
        last=cur;
    }
    return cur!=1;
}
LL M_R(LL x)
{
    if(x==2)
        return 1;
    if(x<2||!(x&1))
        return 0;
    LL t=x-1;
    int cnt=0;
    while(!(t&1))
    {
        t>>=1;
        ++cnt;
    }
    for(int i=0;i<10;++i)
        if(check(x,p[i],t,cnt))
            return  0;
    return 1;
}
LL Rand()
{
    static LL seed=233233233233233LL;
    seed+=seed<<1|1;
    if(seed<0)
        seed^=(1LL<<63);
    return seed;
}
LL gcd(LL a,LL b)
{
    if(a<0)a=-a;
    if(b<0)b=-b;
    LL t;
    while(b)
    {
        t=a;
        a=b;
        b=t%b;
    }
    return a;
}
LL p_rho(LL x,int c)
{
    LL x0=Rand()%(x-1)+1,y,i=1,j=2,ans;
    y=x0;
    while(1)
    {
        ++i;
        (y=mul(y,y,x)+c)%x;
        ans=gcd(y-x0,x);
        if(ans!=1&&ans!=x)
            return ans;
        if(y==x0)
            return x;
        if(i==j)
        {
            j<<=1;
            x0=y;
        }
    }
}
LL find_fac(LL x)
{
    if(M_R(x))
        return x;
    int t=1;
    LL ans;
    while((ans=p_rho(x,t))==x)
        ++t;
    return ans;
}
bool can(int x)
{
    ans.clear();
    int i,j;LL t,s;
    for(i=2;i<=10;++i)
    {
        s=0;
        for(t=1LL,j=x;j;j>>=1,t*=i)
            s+=(j&1)*t;
        if(M_R(s))
            return 0;
        else ans.push_back(find_fac(s));
    }
    return 1;
}
void output(int x)
{
    int stk[60],top=0;
    while(x)
    {
        stk[top++]=x&1;
        x>>=1;
    }
    for(--top;top>=0;--top)
        putchar(stk[top]+'0');
    for(vector<int>::iterator it=ans.begin();
        it!=ans.end();++it)
            printf(" %d",*it);
    putchar('\n');
}
int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        printf("Case #%d:\n",t);
        scanf("%d%d",&n,&j);
        int i,k,tt=1<<(n-2);
        for(i=0;i<tt;++i)
        {
            k=1<<(n-1);
            (k|=(i<<1))|=1;
            if(can(k))
            {
                --j;
                output(k);
                if(!j)break;
            }
        }

    }
    return 0;
}
