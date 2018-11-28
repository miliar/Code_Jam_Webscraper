#include <bits/stdc++.h>

using namespace std;

#define LL long long
#define PB push_back
#define FL(i, n, m)		for(int i=n; i<m; i++)
#define FLN(i, n)		for(int i=0; i<n; i++)
#define INT_INF 2000000000
#define LL_INF 4000000008000000004
#define ALL(x)	(x).begin(), (x).end()
#define MP(x, y)	make_pair((x), (y))
#define PI 3.14159
#define VI vector<int>
#define VVI vector<VI >
#define VL vector<LL>
#define VVL vector<VL >
#define MOD 1000000007
#define PII pair<int,int>
#define VPII vector<PII>
#define VVPII vector<VPII>
#define PLL pair<LL, LL>
#define VPLL vector<PLL>
#define VVPLL vector<VPLL >
#define F first
#define S second

int main()
{
    ios_base::sync_with_stdio(false);
    cout.precision(20);
	int t,smax,temp,cnt,n;
	string s;
	cin>>t;
	FL(l,1,t+1)
	{
		cin>>smax>>s;
		cnt=0;
		temp=s[0]-'0';
		n=s.length();
		FL(i,1,n)
		{
			cnt+=max(0,i-temp-cnt);
			temp+=s[i]-'0';
		}
		cout << "Case #" << l << ": " << cnt << endl ;
	}
}
