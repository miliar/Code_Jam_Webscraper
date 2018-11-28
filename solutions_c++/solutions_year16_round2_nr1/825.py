#include <bits/stdc++.h>

using namespace std;

string digs[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string repr = "ZWXUSGOTFN";
int nms[] = {0, 2, 6, 4, 7, 8, 1, 3, 5, 9};

signed main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		string s;
		cin >> s;
		int cnt[128];
		memset(cnt, 0, sizeof(cnt));
		for(auto it: s)
			cnt[it]++;
		int nums[10];
		memset(nums, 0, sizeof(nums));
		for(int i = 0; i < 10; i++)
		{
			while(cnt[repr[i]])
			{
				for(auto it: digs[nms[i]])
					cnt[it]--;
				nums[nms[i]]++;
			}
		}
		for(int i = 0; i < 10; i++)
			cout << string(nums[i], '0' + i);
		cout << "\n";
	}
	return 0;
}
