#include <bits/stdc++.h>

#define sf scanf
#define pf printf
#define mp make_pai
#define ll long long int

using namespace std;

int main()
{
	int T;	cin >> T;
	for(int t = 0; t < T; t++)
	{
		string S;
		cin >> S;
		string ans;
		ans += S[0];
		for(int i = 1; i < S.size(); i++)
		{
			if(S[i] >= ans[0])
			{
				string tmp;	tmp += S[i];	tmp += ans;
				ans = tmp;
			}
			else
			{
				ans += S[i];
			}
		}
		pf("Case #%d: ", t+1);
		cout << ans << endl;
	}
	return 0;
}
