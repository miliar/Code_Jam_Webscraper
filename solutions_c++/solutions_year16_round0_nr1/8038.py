#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define pii pair< int , int >
#define vii vector< int >
#define ff first
#define ss second
#define rep(i,n) for(int i=0;i<n;i++)
#define frep(i , a , b) for(int i = a;i <= b;i++)
#define fast cin.sync_with_stdio(0);cin.tie(0);
#define CASES int t;cin >> t;while(t--)
#define FI freopen ("in.txt", "r", stdin)
#define FO freopen ("out.txt", "w", stdout)

const int MOD = 1e9 + 7;

int main()
{
	FI;
	FO;
	int t;
	cin>>t;
	frep(i,1,t)
	{
		cout<<"Case #"<<i<<": ";
		ll n;
		cin>>n;
		set<ll> s;
		if(n==0)
			cout<<"INSOMNIA\n";
		else
		{
			ll x,m=1;
			while(s.size()!=10)
			{
				x=n*m;
				m++;
				while(x)
				{
					s.insert(x%10);
					x/=10;
				}
			}
			cout<<n*(m-1)<<"\n";
		}
	}
	return 0;
}