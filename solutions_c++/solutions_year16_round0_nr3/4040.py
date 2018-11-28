#include <iostream>
#include <math.h>
#include <stdio.h>
typedef long long ll;
using namespace std;
ll prime[4000000],number=1,po[11][18];
FILE *f=freopen("test.in","rt",stdin);
FILE *f1=freopen("output.ou","wt",stdout);
void make_prime_array()
{
    prime[0]=2;
    for (ll i=3;i<=33333334;i++)
    {
        bool check=true;
        for (ll j=0;j<number;j++)
        if (i%prime[j]==0)
        {
            check=false;
            break;
        }
        else if (prime[j]>=(ll)sqrt(i)) break;
        if (check) prime[number++]=i;
    }
    for (int i=2;i<=10;i++)
    {
        po[i][0]=1;
        for (int j=1;j<=17;j++) po[i][j]=po[i][j-1]*i;
    }
}
bool isprime(ll value,ll &res)
{
    for (ll i=0;i<number;i++)
        if (value%prime[i]==0)
        {
            res=prime[i];
            return false;
        }
        else if (prime[i]>(ll)sqrt(value)) break;
    return true;
}
ll ok(ll res[], ll ca,ll res1[])
{
    ll value;
    for (ll i=2;i<=10;i++)
    {
        value=0;
        for (ll j=1;j<=ca;j++)
        if (res[j]==1) value+=po[i][ca-j];
        if (isprime(value,res1[i])) return false;
    }
    return true;
}
void build(ll da, ll ca, ll res[], ll res1[], ll &cou, ll total)
{
    if (cou>=total) return;
    if (da>=ca)
    {
        if (ok(res,ca,res1))
        {
            for (ll i=1;i<=ca;i++) cout<<res[i];
            cout<<' ';
            for (ll i=2;i<=10;i++) cout<<res1[i]<<' ';
            cout<<endl;
            cou++;
        }
        return;
    }
    for (ll i=0;i<2;i++)
    {
        res[da]=i;
        build(da+1,ca,res,res1,cou,total);
    }
}
int main()
{
    ll t;
    ll n,j,cou=0,a[17],b[10],st=0;
    make_prime_array();
    cin>>t;
    for (ll c=0;c<t;c++)
    {
        cin>>n>>j;
        cout<<"Case #"<<c+1<<':'<<endl;
        a[1]=1;
        a[n]=1;
        build(2,n,a,b,st,j);
    }
    return 0;
}
