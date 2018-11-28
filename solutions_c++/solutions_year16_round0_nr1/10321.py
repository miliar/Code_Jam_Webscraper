#include <bits/stdc++.h>

using namespace::std;

#define ll long long int
#define mp make_pair
#define ff first
#define ss second
const int MOD=1000000007,INF = 1e9,MAX = 2e6;


ll a[MAX],b[MAX],C[MAX];
vector < ll >  v;

ll check[20];
ll va[1000001];

void init()
{
	for(ll i=0;i<10;i++)
	check[i]=0;	
}

bool verify()
{
	for(ll i=0;i<10;i++)
	{
		if(check[i]==0)
		return true;	
	}

	return false;
}

void update(int n)
{
	while(n>0)
	{
		ll val = n%10;
		n=n/10;
		check[val]++;
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);

	ll i,j,k,n,t;

	//cin>>t;


	cin>>t;

	for(i=1;i<=t;i++)
	{
		cin>>n;

		if(n==0)
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
		{
			init();

			ll count = 0;
			ll ans;

			while(verify())
			{
				ll temp = (count+1)*n;

				update(temp);
				count++;
				ans = temp;
				
			}
		cout<<"Case #"<<i<<": "<<ans<<endl;

		}	
	}

} 
