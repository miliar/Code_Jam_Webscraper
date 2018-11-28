#include <bits/stdc++.h>

using namespace std;
const int mod = 1e9+7;

int main(void)
{
// #ifndef ONLINE_JUDGE
// 	freopen("input.txt","r",stdin);
// 	freopen("output.out","w",stdout);
// #endif
	long long int t,TestCase,i,n;
	cin >> TestCase;
	for(t = 1; t <= TestCase; t++)
	{
		long long int ans = 0,res;
		string s;
		cin >> n >> s;
		res = int(s[0])-48;
		for(i = 1; i <= n; i++)
		{
			if(res < i)
			{
				ans += i-res;
				res += i-res;
			}
			res+=int(s[i])-48;
		}
		cout << "Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
