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

int main()
{
	FAST1;
	FAST2;
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		string s;
		cin>>s;
		int n = s.length();
		int res = 0;
		while(1)
		{
			int x = -1;
			for(int i = n-1; i >= 0; --i)
			{
				if(s[i] == '-')
				{
					x = i;
					break;
				}
			}
			if(x == -1)
				break;
			for (int i = 0; i <= x; ++i)
			{
				if(s[i] == '+')
					s[i] = '-';
				else
					s[i] = '+';
			}
			++res;
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
	return 0;
}