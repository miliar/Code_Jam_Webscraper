#include <bits/stdc++.h>
#define ll long long
using namespace std;
void print(ll a[], ll i)
{
    ll j;
    for(j=i-1;j>=0;j--)
        cout<<a[j];
    cout<<endl;
}
ll fillarray(ll n, ll co, ll a[])
{
    ll x, i=0, c=0;
    while(n>0)
    {
        x=(n%10)*co+c;
        a[i]=x%10;
        c=x/10;
        n/=10;
        i++;
    }
    while(c!=0)
    {
        a[i]=c%10;
        c/=10;
        i++;
    }
    return i;
}
int main()
{
    ll t, r, n, co, b, c, y, i;
    cin>>t;
    r=t;
    while(t--)
    {
        cin>>n;
        if(n==0)
            cout<<"Case #"<<r-t<<": INSOMNIA"<<endl;
        else
        {
            cout<<"Case #"<<r-t<<": ";
            ll h[10];
            for(i=0;i<10;i++)
                h[i]=1;
            co=0;b=1;
            while(true)
            {
                c=0;
                for(i=0;i<10;i++)
                    if(h[i]!=1)
                        c++;
                if(c==10)
                    break;
                y=n*b;
                while(y>0)
                {
                    ll r=y%10;
                    if(h[r]!=0)
                        h[r]=0;
                    y=y/10;

                }
                co++;b++;
            }
            ll a[100000];
            memset(a,0,sizeof(a));
            i=fillarray(n,co,a);
            print(a,i);
        }
    }
    return 0;
}