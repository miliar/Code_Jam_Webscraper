#include<bits/stdc++.h>

using namespace std;

#define pb push_back
#define mem(a, b) memset(a, b, sizeof(a))
#define mp make_pair

const int oo = (int)1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	for(int c=1;c<=t;++c)
	{
		int n;
		string s;
		cin >> n >> s;
		int sum = 0;
		int ans = 0;
		for(int i=0;i<(int)s.size();++i)
		{
			if(sum < i)
			{
				ans += i-sum;
				sum = i;
			}
			sum += s[i]-'0';
		}
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}
