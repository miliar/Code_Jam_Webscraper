#include <bits/stdc++.h>
#include "utils.h"
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

//ashu

using namespace std;


struct Obj
{
	string chr;
	char stages[13][4096];
	int p, r, s;

	static char findd(char c1, char c2)
	{
		if ((c1 == 'P' && c2 == 'R') ||
			(c1 == 'R' && c2 == 'S') || 
			(c1 == 'S' && c2 == 'P'))
		{
			return c1;
		}
		return c2;
	}

	bool ester(int pos)
	{
		if (p == 0 && r == 0 && s == 0)
		{
			return true;
		}
		if (p > 0 && r > 0)
		{
			--p;
			--r;
			chr[pos] = 'P';
			chr[pos + 1] = 'R';
			int idx2 = pos / 2;
			stages[0][idx2] = 'P';
			int step = 0;
			bool flag = true;
			while (idx2 % 2 == 1)
			{
				if (stages[step][idx2] == stages[step][idx2 - 1])
				{
					flag = false;
					break;
				}
				stages[step + 1][idx2 / 2] = findd(stages[step][idx2], stages[step][idx2 - 1]);
				++step;
				idx2 /= 2;
			}
			if (flag && ester(pos + 2))
			{
				return true;
			}
			++r;
			++p;
		}
		if (p > 0 && s > 0)
		{
			--p;
			--s;
			chr[pos] = 'P';
			chr[pos + 1] = 'S';
			int idx2 = pos / 2;
			stages[0][idx2] = 'S';
			int step = 0;
			bool flag = true;
			while (idx2 % 2 == 1)
			{
				if (stages[step][idx2] == stages[step][idx2 - 1])
				{
					flag = false;
					break;
				}
				stages[step + 1][idx2 / 2] = findd(stages[step][idx2], stages[step][idx2 - 1]);
				++step;
				idx2 /= 2;
			}
			if (flag && ester(pos + 2))
			{
				return true;
			}
			++s;
			++p;
		}
		if (r > 0 && s > 0)
		{
			--r;
			--s;
			chr[pos] = 'R';
			chr[pos + 1] = 'S';
			int idx2 = pos / 2;
			stages[0][idx2] = 'R';
			int step = 0;
			bool flag = true;
			while (idx2 % 2 == 1)
			{
				if (stages[step][idx2] == stages[step][idx2 - 1])
				{
					flag = false;
					break;
				}
				stages[step + 1][idx2 / 2] = findd(stages[step][idx2], stages[step][idx2 - 1]);
				++step;
				idx2 /= 2;
			}
			if (flag && ester(pos + 2))
			{
				return true;
			}
			++s;
			++r;
		}
		return false;
	}
};

Output solve(Input input)
{
	Obj r;
	r.p = input.p;
	r.r = input.r;
	r.s = input.s;
	r.chr = std::string(r.p + r.r + r.s, ' ');
	if (r.ester(0))
	{
		return{ r.chr };
	}
	return{ "IMPOSSIBLE" };
}

struct Input
{
	int n, p, r, s;
	istream& operator >> (istream& x, Input& y)
	{
		return x >> y.n >> y.r >> y.p >> y.s;
	}
};

struct Output
{
	string s;

	ostream& operator << (ostream& x, const Output& y)
	{
		static int case_number = 0;
		return x << "Case #" << ++case_number << ": " << y.s << endl;
	}
};

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		Input input;
		fin >> input;
		auto ans = solve(input);
		return ans;
	}
	return 0;
}