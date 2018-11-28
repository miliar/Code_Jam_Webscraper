#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define sd(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)

int main()
{
	int t;
	cin >> t;
	for(int tc=1;tc<=t;++tc)
	{
		string s, res;
		cin >> s;
		res = s[0];
		for(int i=1;i<s.size();++i)
			if(s[i]>=res[0])
				res = s[i] + res;
			else
				res += s[i];
		cout << "Case #" << tc << ": " << res << endl;
	}
	return 0;
}
