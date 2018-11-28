#include<bits/stdc++.h>
#define ull unsigned long long
#define MAX 100000001
#define LEN 6550
#define LMT 10001
using namespace std;

bool chk_prime[MAX]={0};
vector<int> primes;
vector<int> ans;

void sieve()
{
	chk_prime[0]=chk_prime[1]=1;
	for(int i=2; i<LMT; i++)
	{
		if(!chk_prime[i]) {
			for(int j=i*2; j<MAX; j+=i)
			{
				chk_prime[j]=1;
			}
		}
	}
	for(int i=2; i<MAX; i++)
	{
		if(!chk_prime[i]) primes.push_back(i);
	}
}

bool chk(int n)
{
	if(n<MAX) {
		if(chk_prime[n]) return 0;
		else return 1;
	}
	else {
		for(int i=0; primes[i]<=sqrt(n); i++)
		{
			if(n%primes[i]==0) return 0;
		}
		return 1;
	}
}

int num[32];

bool base_value(int base)
{
	//cout<<"enter base value"<<endl;
	/*long long res=1;
	for(int i=30; i>=0; i--)
	{
		if(num[i]==1) {
			res+=base;
		}
		//res=res*base+num[i];
	}
	res=res*base+1;*/
	//cout<<" "<<res<<endl;
	//for(int i=0; primes[i]<=sqrt(res); i++)
	for(int i=0; i<primes.size(); i++)
	{
		long long p=1,t=base;
		for(int j=30; j>=0; j--)
		{
			if(num[j]==1) {
				p+=t;
			}
			t=(t*base)%primes[i];
			p=p%primes[i];
		}
		//p=(p*base+num[i])%primes[i];
		p=p%primes[i];
		if(p==0) {
			ans.push_back(primes[i]);
			return 1;
		}
		/*if(res%primes[i]==0) {
			ans.push_back(primes[i]);
			return 1;
		}*/
	}
	return 0;
}

bool calc(int n)
{
	//cout<<"enter calc"<<endl;
	int index=30;
	while(n>0)
	{
		num[index]=n%2;
		n/=2;
		index--;
	}
	int value;
	bool flag=0;
	for(int i=2; i<=10; i++)
	{
		if(!base_value(i)) {
			ans.clear();
			return 0;
		}
	}
	return 1;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	sieve();
	freopen("C:/Users/HP/Desktop/CodeJam/test.txt","r",stdin);//redirects standard input
	freopen("C:/Users/HP/Desktop/CodeJam/output.txt","w",stdout);//redirects standard output
	int t,n,j;
	cin>>t;
	for(int tc=1; tc<=t; tc++)
	{
		cin>>n>>j;
		cout<<"Case #"<<tc<<": "<<endl;
		for(int i=0; i<32; i++)
		{
			num[i]=0;
		}
		num[0]=1;
		//num[5]=1;
		num[31]=1;
		int cnt=0;
		for(int i=0; ; i++)
		{
			if(calc(i)) {
				cnt++;
				for(int i=0; i<32; i++)
				{
					cout<<num[i];
				}
				cout<<" ";
				for(int i=0; i<ans.size(); i++)
				{
					cout<<ans[i]<<" ";
				}
				cout<<endl;
				ans.clear();
				if(cnt==j) break;
			}
		}
	}
	return 0;
}
