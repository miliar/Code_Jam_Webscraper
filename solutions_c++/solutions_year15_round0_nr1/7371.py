#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

#define REP(i,k,n) for(int i=k;i<n;i++)
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int main()
{
	int t;
	cin >> t;

	rep(q,t)
	{
		int n;
		string s;

		cin >> n >> s;

		int cnt[1005];
		memset(cnt,0,sizeof(cnt));

		cnt[0] = s[0] - '0';
		int ans = 0;

		REP(i,1,s.size())
		{
			int d = s[i] - '0';

			if(cnt[i-1] < i)
			{
				int diff = i - cnt[i-1];
				ans += diff;
				cnt[i-1] += diff;
			}

			cnt[i] = cnt[i-1] + d;
		}

		cout << "Case #" << q+1 << ": " << ans << endl; 

	}
	
	return 0;
}
