#include<bits/stdc++.h>
#define ll long long int
using namespace std;

ll a[10];

void initialise()
{
    for(int i=0;i<10;i++) a[i]=0;
}

bool f(ll n)
{
    ll temp,rem;
    temp=n;
    while(temp!=0)
    {
        rem=temp%10;
        a[rem]++;
        temp/=10;
    }
    int f=0;
    ll c=0;
    for(int i=0;i<10;i++)
    {
        if(a[i]>0) c++;
    }
    if(c==10) f=1;

    if(f==1) return true;
    else return false;
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
	ll t; cin>>t;
    for(ll k=1;k<=t;k++)
	{
	    initialise();
	    ll n,i;
	    cin>>n;
	    if(n==0) cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
	    else
	    {
	    ll temp=n;
	    ll q=2;
	    while(!f(temp))
	    {
	       temp=q*n;
	       q++;
	    }
	    cout<<"Case #"<<k<<": "<<temp<<endl;
	    }
	}
	return 0;
}
