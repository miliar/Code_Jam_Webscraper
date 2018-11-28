#include<bits/stdc++.h>
#define ll long long int
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
int Set(int n,int pos) {return n | (1<<pos);}
int Reset(int n,int pos){return n & ~(1<<pos);}
int Check(int n,int pos){return n & (1<<pos);}
using namespace std;
ll b[11],a,n,J;
struct data
{
    ll d[11],coin;
};
vector<data>v;
ll pow(ll n,ll idx)
{
    ll i,ans;
    for(ans=1,i=1;i<=idx;i++)
    {
        ans*=n;
    }
    return ans;
}
ll check_prime(ll n)
{
    ll lim=sqrt(n)+1;
    for(ll i=2;i<=lim;i++)
    {
        if(n%i==0)
        {
            return i;
        }
    }
    return 0;
}
void solve(ll num)
{
    memset(b,0,sizeof(b));
    ll i,j,base;
    for(j=0;j<n;j++)
    {
        for(base=2;base<=10;base++)
        {
            if(Check(num,j))
            {
                b[base]+=pow(base,j);
            }
        }
    }
    ll temp[11],cnt=0;
    for(i=2;i<=10;i++)
    {
        temp[i]=check_prime(b[i]);
        if(temp[i])
        {
            cnt++;
        }
    }
    if(cnt==9)
    {
        data c;
        c.coin=num;
        for(i=2;i<=10;i++)
            c.d[i]=temp[i];
        v.push_back(c);
    }
}
void gen(ll num,ll pos)
{
    if(v.size()==J)
        return;
    if(pos==n-2)
    {
        solve(num);
        return;
    }
    gen(num,pos+1);
    if(Check(num,pos))
        gen(Reset(num,pos),pos+1);
    else
        gen(Set(num,pos),pos+1);
}
void print(ll num)
{
    for(int i=n-1;i>=0;i--)
    {
        if(Check(num,i))
            printf("1");
        else
            printf("0");
    }
    printf(" ");
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,T=0;
    sl(t);
    while(t--)
    {
        sl(n); sl(J);
        a=0;
        a=Set(a,0);
        a=Set(a,n-1);
        gen(a,1);
        printf("Case #%lld:\n",++T);
        for(int i=0;i<v.size();i++)
        {
            print(v[i].coin);
            for(int j=2;j<10;j++)
                printf("%lld ",v[i].d[j]);
            printf("%lld\n",v[i].d[10]);
        }
    }
    return 0;
}
