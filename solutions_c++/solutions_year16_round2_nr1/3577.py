#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ifstream fin("1.in");
ofstream fout("1.out");

//int count = 10;
string digits[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int d = 1000;
int p[2000] = {};
string s;
int t;
int cnt;
int dcnt;
int ans[2000] = {};

void rem(int num)
{
	for (char c : digits[num])
	{
		p[c + d]--;
		dcnt--;
	}
}

void add(int num)
{
	for (char c : digits[num])
	{
		p[c + d]++;
		dcnt++;
	}
}

bool exist(int num)
{
	map<char, int> m;
	for (char c : digits[num])
		m[c]++;
	bool result = true;
	for (auto el : m)
	{
		result &= (p[el.first + d] >= el.second);
	}
	return result;
}

bool getAns()
{
	if (dcnt == 0)
		return true;
	for (int i = 0; i < 10; i++)
	{
		if (exist(i))
		{
			rem(i);
			ans[cnt++] = i;
			bool res = getAns();
			if (res)
				return true;
			add(i);
			cnt--;
		}
	}
	return false;
}

int main(int argc, char *argv[])
{
	fin >> t;
	for (int qq = 0; qq < t; qq++)
	{
		fin >> s;
		fout << "Case #" << qq + 1 << ": ";
		for (int i = 0; i < 2000; i++)
			p[i] = 0;
		for (char c : s)
		{
			p[c + d]++;
		}
		dcnt = s.length();
		cnt = 0;
		getAns();
		sort(ans, ans + cnt);
		int sum = 0;
		for (int i = 0; i < cnt; i++)
		{
			fout << ans[i];
			sum += digits[ans[i]].length();
		}
		fout << "\n";
		assert(sum == s.length());
	}
	//cout << "OK";
	return 0;
}
