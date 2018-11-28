#include <bits/stdc++.h>
using namespace std;
#define ReadFile freopen("I:/CODE/CodeJam/A-small-attempt1.in","r",stdin)
#define WriteFile freopen("I:/CODE/CodeJam/A-small-attempt1-out.txt","w",stdout)
#define Boost ios_base::sync_with_stdio(false)
#define setP(s,p) fixed<<setprecision(p)<<ssss
#define pb emplace_back
#define MOD 1000000007
#define MAX 27
#define INF LONG_MAX
#define f first
#define s second
#define endl '\n'

typedef long long int ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

pair<ll,char> arr[MAX];
ll inp[MAX];

int main()
{
	ReadFile;
	WriteFile;
	Boost;
	ll t,n;
	cin>>t;
	for(ll l = 1; l <= t; l++)
	{
		cin>>n;
		for(ll i = 1; i <= n; i++)
		{
			cin>>inp[i];
			arr[i] = {inp[i],i};
		}
		sort(arr + 1, arr + n + 1);
		ll ind1 = arr[n].s;
		ll ind2 = arr[n - 1].s;
		cout<<"Case #"<<l<<": ";
		if(inp[ind1] > inp[ind2])
		{
			if(inp[ind1] - inp[ind2] == 2)
			{
				cout<<(char)(64 + ind1);
				inp[ind1]--;
			}
			cout<<(char)(64 + ind1)<<" ";
			inp[ind1]--;
		}
		for(ll i = 1; i <= n; i++)
		{
			if(i == ind1 || i == ind2) continue;
			while(inp[i] > 0)
			{
				if(inp[i] >= 2)
				{
					cout<<(char)(64 + i)<<(char)(64 + i)<<" ";
					inp[i] -= 2;
				}
				else 
				{
					cout<<(char)(64 + i)<<" ";
					inp[i]--;
				}
			}
		}
		while(inp[ind1] > 0)
		{
			cout<<(char)(64 + ind1)<<(char)(64 + ind2)<<" ";
			inp[ind1]--;
			inp[ind2]--;
		}
		cout<<endl;
	}
	return 0;
}

