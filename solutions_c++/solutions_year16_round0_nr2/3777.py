#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<memory.h>
#include<map>
#include<string>
using namespace std;

string s;
/*int d[1000][2][2];

map<string, int> m;
map<string, string> p;
string q[100000];
int qh, qt;

int brute()
{
	while (qh < qt)
	{
		string s = q[qh++];
		bool b = false;
		for (int i = 0; i < s.length(); ++i)
		if (s[i] == '-') b = true;
		if (!b) return m[s];
		for (int i = 1; i <= s.length(); ++i)
		{
			string w = s;
			reverse(w.begin(), w.begin() + i);
			for (int j = 0; j < i; ++j)
			if (w[j] == '-') w[j] = '+'; else w[j] = '-';
			if (m.count(w)) continue;
			m[w] = m[s] + 1;
			p[w] = s;
			q[qt++] = w;
		}
	}
}*/
int answer;

void solve()
{
	/*cin >> s;
	m.clear();
	p.clear();
	m[s] = 0;
	p[s] = "";
	qh = qt = 0;
	q[qt++] = s;
	int ans = brute();
	answer = ans;
	printf("%d", ans);
	//string c = "";
	//for (int i = 0; i < s.length(); ++i) c.push_back('+');
	//while (c != "") cout << c << "\n", c = p[c];
	/*reverse(s.begin(), s.end());
	for (int i = 0; i < 1000;++i)
	for (int j = 0; j < 2;++j)
	for (int k = 0; k < 2; ++k) d[i][j][k] = 1000000;
	if (s[0] == '-')
	{
	d[0][0][0] = 0;
	d[0][1][1] = 1;
	}
	else
	{
	d[0][1][0] = 1;
	d[0][0][1] = 0;
	}

	for (int i = 1; i < s.length(); ++i)
	{
	if (s[i] == '+')
	{
	d[i][0][1] = d[i - 1][0][1];
	d[i][1][1] = d[i - 1][1][1];
	d[i][0][0] = d[i - 1][1]
	}
	else
	{

	}
	}
	return d[s.length() - 1];*/
}

void solve2()
{
	cin >> s;
	int d = 1;
	for (int i = 1; i < s.length(); ++i)
	if (s[i] != s[i - 1]) d++;
	if (s[s.length() - 1] == '+') d--;
	printf("%d", d);
	//if(d!=answer) printf("asgdksjadasd");
}

int main()
{
	ios::sync_with_stdio(0);
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		printf("Case #%d: ", test);
		//solve();
		solve2();
		printf("\n");
	}
	return 0;
}