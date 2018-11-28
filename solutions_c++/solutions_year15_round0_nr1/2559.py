#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,n;
	string s;
	cin >> t;
	for(int test=1;test<=t;++test)
	{
		cin >> n;
		cin >> s;
		int cnt = 0, cur = 0;
		for(int i=0;i<s.size();++i)
		{
			int x = s[i]-'0';
			if(cur<i)
			{
				cnt += (i-cur);
				cur += (i-cur);
			}
			cur += x;
		}
		cout << "Case #" << test << ": " << cnt << endl;
	}
	return 0;
}
