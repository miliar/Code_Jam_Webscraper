#include<bits/stdc++.h>
using namespace std;

#define ll long long int
ll arr[12]={2,3,5,7,11,13,17,19,23,29,31,37};
ll mulmod(ll a , ll b, ll mod)
{
	ll x=0,y=a%mod;
	while(b)
	{
		if(b&1)  x = (x+y)%mod;
			 y = (y<<1)%mod;
			 b>>=1;
	}
	return x;
}

ll po(ll a,ll b,ll mod)
{
	ll x=1, y=a;
	while(b)
	{
		if(b&1) x=mulmod(x,y,mod);
		y=mulmod(y,y,mod);
		b>>=1;
	}
	return x;
}

bool isprime(ll n)

{
	if(n<2) return false;
	if(n!=2&&n%2==0)  return false;
	if(n==2||n==3)  return true;
	ll s = n-1;
	while(s%2==0)
	  {
	  	 s=s/2;
	  }
	for(int j=0;j<10;j++)
	{
		ll temp = s;
	ll a = arr[j];
	ll mod = po(a,s,n);
	if(mod ==-1||mod==1)
	  continue;
	while(temp!=n-1&&mod!=n-1)
	{
		mod = mulmod(mod,mod,n);
		temp<<=1;
	}
	if(mod!=n-1)
	  return false;

}
 return true;
}

ll power_of_expo[120][210];
void pre_calculation()
{
    for(int i=2;i<=10;i++)
        power_of_expo[i][0]=1;
    for(ll i=2;i<=10;i++)
        for(ll j=1;j<=17;j++)
            power_of_expo[i][j]=power_of_expo[i][j-1]*i;

}

ll base_converter(ll n,ll b)
{
    ll x=0,i=0;
    while(n)
    {
        x+=(n&1)*power_of_expo[b][i];
        n>>=1;
        i++;
    }
    return x;

}
int main()
{
    ofstream fout("output.txt");
    int t;
    cin>>t;
    fout<<"Case #1:"<<endl;

    pre_calculation();   ll n,k;
    cin>>n>>k;
    for(ll i=(1<<15)+1;i<(1<<16);i+=2)
    {

        int f=0;
        ll fact[20];
        int mark=0;

        for(ll b =2;b<=10;b++)
        {
            ll x=base_converter(i,b);

            if(isprime(x))
            {
                mark=1;
                break;
            }
        }
        if(!mark)
        {


        for(ll b =2;b<=10;b++)
        {
            ll x=base_converter(i,b);
            for(int j=2;j*j<=x;j++)
            {
                if(x%j==0)
                {
                    fact[b]=j;
                    break;
                }
            }

        }


            k--;
            for(int j=15;j>=0;j--)
            {
                fout<<(1&(i>>j));
            }
            fout<<" ";
            for(int j=2;j<=10;j++)
                fout<<fact[j]<<" ";
            fout<<endl;
            if(k==0)break;


        }
    }

}
