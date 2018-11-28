#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <functional>

using namespace std;

#define ll long long
#define vt vector
#define mod 1000000007

string s, o;
vector<string> nos{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int freq[26] = { 0 };
int cnt = 0;

bool possible(int x)
{
	int cf[26] = { 0 };
	for (int i = 0; i < nos[x].length(); i++)
		cf[nos[x][i] - 'A']++;
	for (int i = 0; i < 26; i++)
		if (freq[i] < cf[i])
			return false;
	return true;
}

void reduce(int x)
{
	for (int i = 0; i < nos[x].length(); i++)
		freq[nos[x][i]-'A']--;
}

void cmf()
{
	o = "";
	for (int i = 0; i < s.length(); i++)
		freq[s[i] - 'A']++;
	cnt = s.length();

	int runOrder[] = { 6, 4, 0, 2, 8, 5, 7, 9, 3, 1 };

	for (int i = 0; i < 10; i++)
		while (possible(runOrder[i]))
		{
			reduce(runOrder[i]);
			o += '0' + runOrder[i];
		}
	sort(o.begin(), o.end());
	cout << o << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> s;
		printf("Case #%d: ", cases);
		cmf();
	}
	return 0;
}