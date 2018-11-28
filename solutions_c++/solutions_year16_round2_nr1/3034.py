#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<map>
using namespace std;

int main() {
	//FILE *fin = freopen("A-small-attempt0.in", "r", stdin);
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	//FILE *fout = freopen("A-small-attempt0.out", "w", stdout);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int num[10] = {0};
		string s;
		cin >> s;
		map<char, int> mp;
		for (int i = 0; i < s.size(); i++)
		{
			if (mp.find(s[i])!=mp.end())
			{
				mp[s[i]]++;
			}
			else
			{
				mp[s[i]] = 1;
			}
		}

		if (mp.find('Z') != mp.end())
		{
			num[0] = mp['Z'];
			for (int i = 0; i < num[0]; i++)
			{
				mp['Z']--;
				mp['E']--;
				mp['R']--;
				mp['O']--;
			}
		}

		if (mp.find('W') != mp.end())
		{
			num[2] = mp['W'];
			for (int i = 0; i < num[2]; i++)
			{
				mp['W']--;
				mp['T']--;
				mp['O']--;
			}
		}

		if (mp.find('U') != mp.end())
		{
			num[4] = mp['U'];
			for (int i = 0; i < num[4]; i++)
			{
				mp['F']--;
				mp['O']--;
				mp['U']--;
				mp['R']--;
			}
		}

		if (mp.find('X') != mp.end())
		{
			num[6] = mp['X'];
			for (int i = 0; i < num[6]; i++)
			{
				mp['S']--;
				mp['I']--;
				mp['X']--;
			}
		}

		if (mp.find('G') != mp.end())
		{
			num[8] = mp['G'];
			for (int i = 0; i < num[8]; i++)
			{
				mp['E']--;
				mp['I']--;
				mp['G']--;
				mp['H']--;
				mp['T']--;
			}
		}

		if (mp.find('O') != mp.end())
		{
			num[1] = mp['O'];
			for (int i = 0; i < num[1]; i++)
			{
				mp['O']--;
				mp['N']--;
				mp['E']--;
			}
		}

		if (mp.find('F') != mp.end())
		{
			num[5] = mp['F'];
			for (int i = 0; i < num[5]; i++)
			{
				mp['F']--;
				mp['I']--;
				mp['V']--;
				mp['E']--;
			}
		}

		if (mp['T']) num[3] = mp['T'];
		if (mp['S']) num[7] = mp['S'];
		if (mp['I']) num[9] = mp['I'];

		string result="";
		cout << "Case #" << t << ": ";
		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < num[i]; j++)
			{
				result += to_string(i);
			}
		}
		cout << result;
		cout << endl;

	}
	exit(0);
}
