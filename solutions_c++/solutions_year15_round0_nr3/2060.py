#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <queue>
#include <deque>
#include <functional>
#include <climits>
#include <cassert>
#include <list>

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ABS(a) (((a) > 0) ? (a) : (-(a)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))

using namespace std;
typedef long long ll;

struct element
{
	bool minus;
	char c;
	element()
	{
		c = '1';
		minus = false;
	}
	element(char _c)
	{
		minus = false;
		c = _c;
	}
	element(char _c, bool _minus)
	{
		c = _c;
		minus = _minus;
	}
	element(int code)
	{
		minus = false;
		if (code >= 5)
		{
			minus = true;
			code -= 5;
		}
		if (code == 0)
			c = '1';
		if (code == 1)
			c = 'i';
		if (code == 2)
			c = 'j';
		if (code == 3)
			c = 'k';
	}
	int code()
	{
		int res = 0;
		if (c == 'i') res = 1;
		if (c == 'j') res = 2;
		if (c == 'k') res = 3;
		if (minus) res += 5;
		return res;
	}
};

element operator *(const element& a, const element& b)
{
	element res;
	res.minus = (a.minus ^ b.minus);
	if (a.c == '1')
	{
		res.c = b.c;
		return res;
	}
	if (b.c == '1')
	{
		res.c = a.c;
		return res;
	}
	if (a.c == 'i' && b.c == 'i')
	{
		res.minus = !res.minus;
		res.c = '1';
		return res;
	}
	if (a.c == 'i' && b.c == 'j')
	{
		res.c = 'k';
		return res;
	}
	if (a.c == 'i' && b.c == 'k')
	{
		res.minus = !res.minus;
		res.c = 'j';
		return res;
	}


	/*j ***** */
	if (a.c == 'j' && b.c == 'i')
	{
		res.minus = !res.minus;
		res.c = 'k';
		return res;
	}
	if (a.c == 'j' && b.c == 'j')
	{
		res.minus = !res.minus;
		res.c = '1';
		return res;
	}
	if (a.c == 'j' && b.c == 'k')
	{
		res.c = 'i';
		return res;
	}



	/*  k ******************          */
	if (a.c == 'k' && b.c == 'i')
	{
		res.c = 'j';
		return res;
	}
	if (a.c == 'k' && b.c == 'j')
	{
		res.minus = !res.minus;
		res.c = 'i';
		return res;
	}
	if (a.c == 'k' && b.c == 'k')
	{
		res.minus = !res.minus;
		res.c = '1';
		return res;
	}
}

const int N = 2e4 + 100;
int dp[N][8][10];

string s;

void fill_dp()
{
	dp[s.length()][2][3] = 1;
	for (int pos = s.length() - 1; pos >= 0; pos--)
	{
		for (int state = 0; state <= 2; state++)
		{
			for (int last_code = 0; last_code <= 8; last_code++)
			{
				if (last_code == 4) continue;
				if (dp[pos + 1][state][(element(last_code) * element((char)(s[pos]))).code()])
				{
					dp[pos][state][last_code] = true;
					continue;
				}
				if (state < 2)
				{
					if (state == 0 && last_code == 1 || state == 1 && last_code == 2)
					{
						if (dp[pos + 1][state + 1][element((char)s[pos]).code()])
							dp[pos][state][last_code] = true;
					}
				}
			}
		}
	}
}

element encode(string s)
{
	element res = element((char)('1'));
	for (int i = 0; i < s.length(); i++)
		res = res * element((char)s[i]);
	return res;
}

bool tupoe()
{
	element res = element('1');
	int ind1 = -1;
	for (int i = 0; i < s.length(); i++)
	{
		res = res * s[i];
		if (res.code() == 1)
		{
			ind1 = i;
			break;
		}
	}
	if (ind1 == -1) return false;

	res = element('1');
	int ind2 = -1;
	for (int i = s.length() - 1; i >= 0; i--)
	{
		res = s[i] * res;
		if (res.code() == 3)
		{
			ind2 = i;
			break;
		}
	}

	if (ind2 <= ind1) return false;

	res = element('1');
	for (int i = ind1 + 1; i < ind2; i++)
	{
		res = res * s[i];
	}
	return res.code() == 2;

	/*for (int i = 1; i < s.length(); i++)
	{
		for (int j = i + 1; j < s.length(); j++)
		{
			string s1 = s.substr(0, i);
			string s2 = s.substr(i, j - i);
			string s3 = s.substr(j, s.length() - j);

			if (encode(s1).code() == 1 && encode(s2).code() == 2 && encode(s3).code() == 3) return true;
		}
	}
	return false;*/
}

/*bool f(int pos, int state, int last_code)
{
	if (pos == 4000)
	{
		cout << "";
	}
	if (pos == s.length())
	{
		if (state == 2 && last_code == 3) return true;
		return false;
	}
	if (dp[pos][state][last_code] != -1) return dp[pos][state][last_code];
	
	bool res = false;
	if (f(pos + 1, state, (element(last_code) * element((char)(s[pos]))).code()))
		res = true;
	
	if (state < 2)
	{
		if (state == 0 && last_code == 1 || state == 1 && last_code == 2)
		{
			if (f(pos + 1, state + 1, element((char)s[pos]).code()))
				res = true;
		}
	}

	return dp[pos][state][last_code] = res;
}*/

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	cin >> tests;

	/*element res = element('i') * 'j';
	res = element('j') * 'k';
	res = element('i') * 'i';
	res = element('k') * 'k';
	res = element('j') * 'j';
	res = element('1') * 'k';
	res = element('1') * '1';*/

	for (int q = 0; q < tests; q++)
	{
		s.clear();
		ZERO(dp);
		//NEGATE(dp);
		int l, x;
		cin >> l >> x;
		string temp;
		cin >> temp;
		for (int i = 0; i < x; i++)
			s += temp;
		//if (s.length() > 1000) continue;
		fill_dp();
		cout << "Case #" << q + 1 << ": ";
		if (dp[0][0][element((char)'1').code()])
		//if (tupoe())
		{
			cout << "YES\n";
		}
		else
		{
			cout << "NO\n";
		}
	}

	return 0;
}