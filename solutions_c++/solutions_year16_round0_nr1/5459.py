#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

bool all_seen(bool * cnt)
{
	bool ans = true;
	for (int i = 0; i < 10; i++)  ans = (ans && cnt[i]);
	return ans;
}

void update_cnt(long long num, bool * cnt)
{
	while (num>0)
	{
		cnt[num % 10] = true;
		num = num / 10;

	}
}

int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int num;
		long long cur;

		cin >> num;

		bool cnt[10];
		memset(cnt, false, sizeof(cnt));

		cur = 0;

		
		while (num != 0 && !all_seen(cnt))
		{
			cur += num;
			update_cnt(cur, cnt);
			
		}

		cout << "Case #" << z << ": ";
		if (num == 0) cout << "INSOMNIA" << endl;
		else cout << cur << endl;
	}

	return 0;
}