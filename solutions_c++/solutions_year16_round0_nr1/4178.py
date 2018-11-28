#include <bits/stdc++.h>
using namespace std;
//@author Vidur Katyal
#define endl '\n'
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef pair <int, int> pii;
typedef pair <int, pii> piii;
typedef vector <int> vi;
typedef vector < pii > vpii;
#define DEBUG(x) cerr<<#x<<": "<<x<<endl;
#define FAST1 ios_base::sync_with_stdio(0)
#define FAST2 cin.tie(0);cout.tie(0); cerr.tie(0)
const long double PI = acos(-1.0);
const long double EPS = 1e-9;
const LL MOD = 1000000007;
const LL MAXN = 100010;

bool solve(LL m, map<int, bool> &Map)
{
	while(m)
	{
		Map[m%10] = 1;
		m /= 10;
	}
	return (Map.size() == 10);
}

int main()
{
	FAST1;
	FAST2;
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		LL n;
		cin>>n;
		map <int, bool> Map;
		if(n == 0)
		{
			cout<<"Case #"<<t<<": INSOMNIA\n";
			continue;
		}
		LL i = 1;
		LL m = n;
		while(!solve(m, Map))
			m = n*(++i);
		cout<<"Case #"<<t<<": "<<m<<endl;
	}
	return 0;
}