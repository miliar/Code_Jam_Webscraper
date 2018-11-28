#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>

using namespace std;

#define ll long long
#define vt vector
#define inf 1000000000
#define mod 1000000007

string s;

string ans = "";

map<char, int> arr;

void zero()
{
	int val = min(arr['Z'], min(arr['E'], min(arr['R'], arr['O'])));
	for (int i = 0; i < val; i++)
		ans += '0';
	arr['Z'] -= val;
	arr['E'] -= val;
	arr['R'] -= val;
	arr['O'] -= val;
}

void one()
{
	int val = min(arr['O'], min(arr['N'], arr['E']));
	for (int i = 0; i < val; i++)
		ans += '1';
	arr['O'] -= val;
	arr['N'] -= val;
	arr['E'] -= val;
}

void two()
{
	int val = min(arr['T'], min(arr['W'], arr['O']));
	for (int i = 0; i < val; i++)
		ans += '2';
	arr['T'] -= val;
	arr['W'] -= val;
	arr['O'] -= val;
}

void three()
{
	int val = min(arr['T'], min(arr['H'], arr['R']));
	if (val * 2 <= arr['E'])
	{
		for (int i = 0; i < val; i++)
			ans += '3';
		arr['T'] -= val;
		arr['H'] -= val;
		arr['R'] -= val;
		arr['E'] -= 2 * val;
	}
}

void four()
{
	int val = min(arr['F'], min(arr['O'], min(arr['U'], arr['R'])));
	for (int i = 0; i < val; i++)
		ans += '4';
	arr['F'] -= val;
	arr['O'] -= val;
	arr['U'] -= val;
	arr['R'] -= val;
}

void five()
{
	int val = min(arr['F'], min(arr['I'], min(arr['V'], arr['E'])));
	for (int i = 0; i < val; i++)
		ans += '5';
	arr['F'] -= val;
	arr['I'] -= val;
	arr['V'] -= val;
	arr['E'] -= val;
}

void six()
{
	int val = min(arr['S'], min(arr['I'], arr['X']));
	for (int i = 0; i < val; i++)
		ans += '6';
	arr['S'] -= val;
	arr['I'] -= val;
	arr['X'] -= val;
}

void seven()
{
	int val = min(arr['S'], min(arr['V'], arr['N']));
	if (val * 2 <= arr['E'])
	{
		for (int i = 0; i < val; i++)
			ans += '7';
		arr['S'] -= val;
		arr['V'] -= val;
		arr['N'] -= val;
		arr['E'] -= 2 * val;
	}
}

void eight()
{
	int val = min(arr['E'], min(arr['I'], min(arr['G'], min(arr['H'], arr['T']))));
	for (int i = 0; i < val; i++)
		ans += '8';
	arr['E'] -= val;
	arr['I'] -= val;
	arr['G'] -= val;
	arr['H'] -= val;
	arr['T'] -= val;
}

void nine()
{
	int val = min(arr['I'], arr['E']);
	if (val * 2 <= arr['N'])
	{
		for (int i = 0; i < val; i++)
			ans += '9';
		arr['I'] -= val;
		arr['E'] -= val;
		arr['N'] -= 2 * val;
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tests = 1; tests <= t; tests++)
	{
		cin >> s;
		arr.clear();

		bool check = true;

		for (int i = 0; i < s.length(); i++)
		{
			arr[s[i]]++;
		}

		ans = "";
		zero();
		eight();
		two();
		four();
		six();
		three();
		seven();
		five();
		one();
		nine();

		for (map<char, int>::iterator it = arr.begin(); it != arr.end(); it++)
			if (it->second != 0)
				check = false;
		sort(ans.begin(), ans.end());
		printf("Case #%d: ", tests);
		cout << ans;
		printf("\n");

	}
	return 0;
}