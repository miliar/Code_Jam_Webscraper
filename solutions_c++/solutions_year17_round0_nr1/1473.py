#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
char arr[1001];
ll ans;
bool check(int l,int k)
{
	ans=0;
	// cout<<arr<<endl;
	for(int i=0;i<l;i++)
	{
		if(arr[i]=='1' && i+k<=l)
		{
			ans++;
			// cout<<"one at "<<i<<endl;
			for(int j=i;j<i+k;j++)
			{
				arr[j]=(char)(1-(arr[j]-'0')+'0');
			}
			// cout<<arr<<endl;
		}
	}
	for(int i=0;i<l;i++)
	{
		if(arr[i]=='1')
			return false;
	}
	return true;
}
int main()
{
	ll t;
	cin>>t;
	ll z=1;
	ll n,k;
	while(t--)
	{
		scanf("%s",arr);
		n=strlen(arr);
		scanf("%lld",&k);
		
		cout<<"Case #"<<z<<": ";
		for(int i=0;i<n;i++)
		{
			if(arr[i]=='-')
				arr[i]='1';
			else
				arr[i]='0';
		}

		// cout<<arr<<" "<<n<<" "<<k<<endl;
		if(check(n,k))
		{
			cout<<ans<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		z++;
	}
}