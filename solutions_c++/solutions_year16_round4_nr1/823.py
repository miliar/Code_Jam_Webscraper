#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <math.h>
#include <fstream>
using namespace std;
#define re return
#define LL unsigned long long
#define EPS 0.00000000000001
#define MOD 1000000009
#define INF 1000000000000000000LL
#define K 101
#define N 200

char str[3][20000];
char ch[3];
int n;

bool Less(char *s, char * t, int len)
{
	for (int i = 0; i < len; ++i)
	{
		if (s[i] > t[i]) re false;
		if (s[i] < t[i]) re true;
	}
	re false;
}

void Swap(char *s, char * t, int len)
{
	for (int i = 0; i < len; ++i)
	{
		char tmp = s[i];
		s[i] = t[i];
		t[i] = tmp;
	}
}

void go(char * s, int type, int index, int len)
{
	if (len == 1)
	{
		s[index] = ch[type];
		return;
	}
	int newLen = len / 2;
	int nxt = 0;
	if (type == 0)nxt = 1;
	if (type == 1)nxt = 2;
	if (type == 2)nxt = 0;
	go(s, type, index, newLen);
	go(s, nxt, index + newLen, newLen);

	if (!Less(s + index, s + index + newLen, newLen))
	{
		Swap(s + index, s + index + newLen, newLen);
	}
}

bool Check(char *str, int len, int r, int p, int s)
{
	for (int i = 0; i < len; ++i)
	{
		if (str[i] == 'R')
		{
			if (r <= 0)return false;
			r -= 1;
		}
		if (str[i] == 'P')
		{
			if (p <= 0)return false;
			p -= 1;
		}
		if (str[i] == 'S')
		{
			if (s <= 0)return false;
			s -= 1;
		}
	}
	if (r > 0)return false;
	if (p > 0)return false;
	if (s > 0)return false;
	return true;
}

int main()
{
#ifdef _DINARISIO
	ifstream cin("A-large.in");
	ofstream cout("A.out");
#endif

	ch[0] = 'P';
	ch[1] = 'R';
	ch[2] = 'S';
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": ";

		int r, p, s;
		cin >> n >> r >> p >> s;
		int len = 1;
		for (int i = 0; i < n; ++i)len *= 2;

		bool ok = false;
		for (int i = 0; i < 3; ++i)
		{
			go(str[i], i, 0, len);
			if (Check(str[i], len, r, p, s))
			{
				ok = true;
				if (i != 0)
				{
					Swap(str[i], str[0], len);
				}
			}
		}
		str[0][len] = 0;
		if (!ok)cout << "IMPOSSIBLE";
		else cout << str[0];
		cout << endl;
	}
	re 0;
}