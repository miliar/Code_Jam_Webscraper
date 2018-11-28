#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <list>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <cstring>
#include <tuple>
#include <cassert>

using namespace std;

int cnt[26], totcnt;
string ans;
string nums[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
bool find(int start)
{
	for(int i = start; i < 10; i++)
	{
		//cout << i << ' ' << totcnt << ' ';
		bool safe = true;
		for(int y : nums[i])
		{
			cnt[y - 'A']--;
			totcnt--;
			if(cnt[y - 'A'] < 0) safe = false;
		}
		//cout << totcnt << ' ' << safe << ' ';
		ans.push_back(i + '0');
		//cout << ans << '\n';
		if(safe && totcnt == 0) return true;
		if(safe && find(i)) return true;
		ans.pop_back();
		for(int y : nums[i])
		{
			cnt[y - 'A']++;
			totcnt++;
		}
	}
	return false;
}

int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for(int k = 1; k <= t; k++)
	{
		string s;
		cin >> s;
		ans = "";
		for(int i = 0; i < 26; i++) cnt[i] = 0;
		for(char x : s) cnt[x - 'A']++;
		totcnt = s.size();
		find(0);
		cout << "Case #" << k << ": " << ans << '\n';
	}

	return 0;
}