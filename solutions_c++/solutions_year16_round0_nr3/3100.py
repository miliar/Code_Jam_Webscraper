#include<bits/stdc++.h>
typedef long long int ll;
using namespace std;
int prime[]={2,3,5,7,11,13,17,23,19,31,37,43,41,47,53,61,59};
ll multiply(ll a,ll b,ll mod)
{
	a%=mod;
	b%=mod;
	long double res=a;
	res*=b;
	ll c=ll(res/mod);
	a*=b;
	a=a-c*mod;
	a=a%mod;
	if(a<0)
		a+=mod;
	return a;
}
ll pow(ll a,ll b,ll mod)
{
	ll x=1,y=a;
	while(b)
	{
		if(b&1)
			x=multiply(x,y,mod);
		y=multiply(y,y,mod);
		b>>=1;
	}
	return x;
}
int miller_rabin(ll p)
{
	if(p<2)
		return 1;
	if(p!=2&&!(p&1))
		return 0;
	for(int i=0;i<17;i++)
	{
		if(p==prime[i])
			return 1;
		if(p%prime[i]==0)
			return 0;
	}
	ll s=p-1;
	int count=0;
	while(!(s&1))
	{
		s>>=1;
		count++;
	}
	ll accuracy=2;
	for(int i=0;i<accuracy;i++)
	{
		ll a=rand()%(p-1)+1;
		ll mod=p,x;
		x=pow(a,s,mod);
		if(x==1||x==p-1)
			continue;
		int flag=0;
		for(int j=0;j<count;j++)
		{
			x=multiply(x,x,mod);
			if(x==1)
				return 0;
			if(x==p-1)
			{
				flag=1;
				break;
			}
		}
		if(flag==1)
			continue;
		return 0;
	}
return 1;
}
ll power[12][20];
void pre()
{
    for(int i=2;i<=10;i++)
        power[i][0]=1;
    for(ll i=2;i<=10;i++)
        for(ll j=1;j<=17;j++)
            power[i][j]=power[i][j-1]*i;

}

ll fu(ll n,ll base)
{
    ll x=0,i=0;
    while(n)
    {
        x+=(n&1)*power[base][i];
        //cout<<(n&1)<<" "<<power[base][i]<endl;
        n/=2;
        i++;
    }
    return x;

}
int main()
{
   // ifstream fin("input.txt");
    ofstream fout("output.txt");
    int t;
    cin>>t;
    fout<<"Case #1:"<<endl;

    pre();
//    cout<<fu(15,2);
    ll n,abc;
    cin>>n>>abc;
    for(ll i=(1<<15)+1;i<(1<<16);i+=2)
    {

        int f=0;
        ll factor[20];
        int flag=0;

        for(ll base =2;base<=10;base++)
        {
            ll x=fu(i,base);

            if(miller_rabin(x))
            {
                flag=1;
                break;
            }
        }
        if(!flag)
        {


        for(ll base =2;base<=10;base++)
        {
            ll x=fu(i,base);
            for(int j=2;j*j<=x;j++)
            {
                if(x%j==0)
                {
                    factor[base]=j;
                    break;
                }
            }

        }


            abc--;
//            fout<<fu(i,2)<<" "<<i<<" ";
            for(int j=15;j>=0;j--)
            {
                fout<<(1&(i>>j));
            }
            fout<<" ";
            for(int j=2;j<=10;j++)
                fout<<factor[j]<<" ";
            fout<<endl;
            if(abc==0)break;


        }
    }

}
