#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<utility>

#define ll long long int
#define F first
#define S second
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define rep(i,in1,n) for(i=in1;i<=n;i++)
#define repd(i,in1,n) for(i=in1;i>=n;i--)

#define pf(n) printf("%d ",n);
#define sf(n) scanf("%d",&n)
#define sl(n) scanf("%I64d",&n)
#define nl printf("\n")
#define mem(arr,init) memset(arr,init,sizeof(arr))
#define vi vector<ll>
#define vvi vector<vi>

#define sz(a) ll((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp make_pair
#define ep emplace_back//c++11
#define ii pair<ll,ll>
#define iii pair<ii,i>
//	freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
using namespace std;
ll prime[1000008];
ll spf[1000008];

bool check1(ll n);

void init()
{
	ll i,j,k;
	for(i=2;i<=1000000;i++)
	{
		if(prime[i]==0)
		{
			for(j=i*i;j<=1000000;j+=i)
			{
				prime[j]=1;
				spf[j]=i;
			}
		}
		
	}
}
ll arr[36];
ll powl(ll a,ll b)
{
	ll ans=1,i,j;
	while(b>=1)
	{
		if(b%2==1)
		{
			ans=ans*a;
		}
		a=a*a;

		b=b>>1;

	}
	return ans;
}
map<ll,ll> map1;
ll flag=0;
bool isprime(ll n)
{
	if(n<=1000000)
	{
		flag=spf[n];
		if(prime[n]==0)
			return true;
		else
			return false;
	}
	else
	{
		ll i,j;
		for(i=2;i*i<=n;i++)
		{
			if(n%i==0)
			{
				flag=i;
				return false;
			}
				
		}
		return true;
	}
}
bool check(ll n)
{
	map1.clear();
	ll val=0;
	ll i;
	//2
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(2,n-i);
		}
	}
//	cout<<"hey "<<val;
//	nl;
	if(isprime(val))
		return false;
	else
		map1[2]=flag;
	//3
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(3,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[3]=flag;

	//4
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(4,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[4]=flag;

	//5
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(5,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[5]=flag;
	//6
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(6,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[6]=flag;
	//7
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(7,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[7]=flag;

	//8
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(8,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[8]=flag;

	//9
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(9,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[9]=flag;
	//10
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(10,n-i);
		}
	}
	if(isprime(val))
		return false;
	else
		map1[10]=flag;


	
	//cout<<"----->   ";
	cout<<val<<" ";
	//nl;
	for(i=2;i<=10;i++)
	{
		cout<<map1[i]<<" ";
	}

	return true;
}

int main()
{
	ll i,j,k,t,n,m,a,b,c,x,y,z,cs;
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	//cout<<powl(2,6);
	cin>>t;
	cin>>n>>z;
	init();
	//cout<<prime[97];
	cout<<"Case #1:";
	nl;
	arr[1]=1;
	arr[n]=1;
	ll no,ans;
	no=0;
	ans=0;
	while(ans<z)
	{
		
		ll tn=no;
		ll p1=n-1;
		while(tn>=1)
		{
			arr[p1]=tn%2;
			p1--;
			tn=tn/2;

		}
	//	cout<<"h1 p1="<<p1;
	//	nl;
		for(i=2;i<=p1;i++)
		{
			arr[i]=0;
		}

		/*for(i=1;i<=n;i++)
			cout<<arr[i];
		nl;*/
		/*if(no==2)
		{
			check1(n);
		}*/
		
		if(check(n))
		{
		//	cout<<"hi";
		//	nl;

		
			ans++;
			nl;
		}

	//	ans++;
		no++;


	}





	return 0;
}
bool check1(ll n)
{
	map1.clear();
	ll val=0;
	ll i;
	//2
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(2,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[2]=val;
	//3
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(3,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[3]=val;

	//4
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(4,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[4]=val;

	//5
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(5,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[5]=val;
	//6
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(6,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[6]=val;
	//7
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(7,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[7]=val;

	//8
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(8,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[8]=val;

	//9
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(9,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[9]=val;
	//10
	val=0;
	for(i=n;i>=1;i--)
	{
		if(arr[i]==1)
		{
			val+=powl(10,n-i);
		}
	}
	cout<<"hey "<<val;
	nl;
	if(prime[val]==0)
		return false;
	else
		map1[10]=val;


	
	//cout<<"----->   ";
	cout<<val<<" ";
	nl;
	for(i=2;i<=10;i++)
	{
		cout<<map1[i]<<" ";
	}

	return true;
}