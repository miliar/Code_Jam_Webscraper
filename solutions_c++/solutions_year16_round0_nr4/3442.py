#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<queue>

#define INF 1000000000
#define endl '\n'
#define ll long long

using namespace std;


ll pow(ll a, ll x)
{
	ll ans=1;
	while(x>0)
	{
		if(x&1)
			ans *= a;
		a *= a;
		x >>= 1;
	}
	return ans;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	for(int t = 1 ; t <= T ; t++)
	{
		cout << "Case #" << t << ": ";
		
		ll n,c,s;
		cin >> n >> c >> s;
//		cout << "n=" << n << ", c=" <<c << ", s=" << s << endl;
		if(s < n)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}
		
		
		ll d=0;
		for(int i = 0 ; i < c ; i++)
			d += pow(n,i);
//		cout << "d=" << d << endl;
		for(int i=0 ; i < n ; i++){
			cout << 1+d*i << " ";
		}
		cout << endl;
	}
	
	return 0;
}

