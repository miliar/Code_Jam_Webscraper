#include<cstdio>
#include<set>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	/*set<string> dictionary[10];

	string nums[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	
	for (int i = 0; i < 10; i++)
	{
		sort(begin(nums[i]), end(nums[i]));

		while (next_permutation(begin(nums[i]), end(nums[i])))
		{
			dictionary[i].insert(nums[i]);
		}
	}

	int nTest; cin >> nTest;
	for (int t = 1; t <= nTest; t++)
	{
		string s, ans="";
		cin >> s;

		int index = 0, curNumber = 0;

		while (1)
		{
			while (index + nums[curNumber].size() >= s.size())
				curNumber++;

			string cur = s.substr(index, nums[curNumber].size());
			index += nums[curNumber].size();

			if (dictionary[curNumber].find(cur) != dictionary[curNumber].end())
			{
				ans += (curNumber + '0');
			}
			else
			{
				curNumber++;
			}
		}

		cout << "Case #" << t << ": " << ans << '\n';
	}*/

	int nTest; cin >> nTest;
	for (int t = 1; t <= nTest; t++)
	{
		string s, ans = "";
		cin >> s;
		int cnt[26];
		for (int i = 0; i < 26; i++) cnt[i] = 0;

		for (int i = 0; i < s.length(); i++)
			cnt[s[i] - 'A']++;

		//find sixes
		int nX = cnt['X' - 'A'];
		for (int i = 0; i < nX; i++)ans += '6';
		cnt['S' - 'A'] -= nX;
		cnt['I' - 'A'] -= nX;

		//find sevens
		int nS = cnt['S' - 'A'];
		for (int i = 0; i < nS; i++)ans += '7';
		cnt['E' - 'A'] -= 2*nS;
		cnt['V' - 'A'] -= nS;
		cnt['N' - 'A'] -= nS;

		//find eights
		 nS = cnt['G' - 'A'];
		for (int i = 0; i < nS; i++)ans += '8';
		cnt['E' - 'A'] -= nS;
		cnt['I' - 'A'] -= nS;
		cnt['H' - 'A'] -= nS;
		cnt['T' - 'A'] -= nS;

		//find tows
		 nX = cnt['W' - 'A'];
		for (int i = 0; i < nX; i++)ans += '2';
		cnt['T' - 'A'] -= nX;
		cnt['O' - 'A'] -= nX;

		//find zeros
		 nS = cnt['Z' - 'A'];
		for (int i = 0; i < nS; i++)ans += '0';
		cnt['E' - 'A'] -= nS;
		cnt['R' - 'A'] -= nS;
		cnt['O' - 'A'] -= nS;

		//find fours
		 nS = cnt['U' - 'A'];
		for (int i = 0; i < nS; i++)ans += '4';
		cnt['F' - 'A'] -= nS;
		cnt['O' - 'A'] -= nS;
		cnt['R' - 'A'] -= nS;

		//find ones
		 nX = cnt['O' - 'A'];
		for (int i = 0; i < nX; i++)ans += '1';
		cnt['N' - 'A'] -= nX;
		cnt['E' - 'A'] -= nX;

		//find threes
		 nS = cnt['T' - 'A'];
		for (int i = 0; i < nS; i++)ans += '3';
		cnt['E' - 'A'] -= 2 * nS;
		cnt['H' - 'A'] -= nS;
		cnt['R' - 'A'] -= nS;
		cnt['S' - 'A'] -= nS;

		//find fives
		 nS = cnt['V' - 'A'];
		for (int i = 0; i < nS; i++)ans += '5';
		cnt['F' - 'A'] -= nS;
		cnt['I' - 'A'] -= nS;
		cnt['E' - 'A'] -= nS;

		//find nines
		 nS = cnt['I' - 'A'];
		for (int i = 0; i < nS; i++)ans += '9';
		cnt['F' - 'A'] -= nS;
		cnt['I' - 'A'] -= nS;
		cnt['E' - 'A'] -= nS;

		sort(ans.begin(), ans.end());

		cout << "Case #" << t << ": " << ans << '\n';
	}

	return 0;
}