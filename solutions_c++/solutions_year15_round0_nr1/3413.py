#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("1.out" , "w" , stdout);
	int t , count;
	cin >> t;
	for(count = 1;count <= t;count++)
	{
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int cnt = s[0] - 48 , ans = 0;
		for(int i = 1;i < s.size();i++)
		{
			if(cnt < i)
			{
				ans += i - cnt;
				cnt += i - cnt;
			}
			cnt += s[i] - 48;
	//		cout << "cnt = " << cnt << endl;
		}
		cout << "Case #" << count << ": " << ans << endl;
	}
	return 0;
}