#include<bits/stdc++.h>
using namespace std;
#define ll  unsigned long long

vector<string> v;

ll mulmod(ll a,ll b)
{
    ll x=0,y=a;
    while(b>0)
    {
        if(b&1)
            x=(x+y);
        y=(y<<1);
        b>>=1;
    }
    return x;
}

ll power(ll a,ll b)
{
    ll x=1,y=a;
    while(b>0)
    {
        if(b&1)
            x=mulmod(x,y);
        y=mulmod(y,y);
        b>>=1;
    }
    return x;
}

ll convert_base(string str,ll base)
{
    ll num=0;
    for(ll i=0;i<str.size();i++)
    {
        num+=(str[i]-48)*power(base,str.size()-i-1);
    }
    return num;
}


int isPrime(ll x)
{
	int div=0;
	if(x%2==0)
	{
		div=2;
		return div;
	}
	for(int i=3;i<=sqrt(x);i+=2)
	{
		if(x%i==0)
		{
			div=i;
			return div;
			break;
		}
	}
	return div;
}

void build_strings(ll n)
{
    string str;
    for(ll i = 0; i < power(2,n); i++)
    {
        str= "";
        ll temp = i;
        for (ll j = 0; j < n; j++)
        {
            if (temp%2 == 1)
                str = '1'+str;
            else
                str = '0'+str;
            temp = temp/2;
        }
        v.push_back("1"+str+"1");
    }
}


int main()
{
	freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
   	vector<ll> divisors;
   	ll test,n,j,num,ans,cnt=0;
   	cin>>test>>n>>j;
    n-=2;
    cout << "Case #" << test << ":\n";
    build_strings(n);
	for(ll i=0;i<v.size() && cnt<j;i++)
    {
        divisors.clear();
        for(ll k=2;k<=10;k++)
        {
            num=convert_base(v[i],k);
            ans=isPrime(num);
            if(ans!=0)
                divisors.push_back(ans);
        }
        if(divisors.size()==9)
        {
            cnt++;
            cout << v[i] << " ";
            for(ll i=0;i<divisors.size();i++)
                cout << divisors[i] << " ";
            cout << "\n"; 
        }
          
    }

    return 0;
}