#include "stdafx.h"
#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

class quat
{
public:
	bool sign;
	char c;
	quat(): sign(true), c('1') {}
};

quat multiple(quat a, quat b)
{
	quat r;
	r.sign = !(a.sign ^ b.sign);
	if (a.c == '1')
	{
		r.c = b.c;
	}
	else if (b.c == '1')
	{
		r.c = a.c;
	}
	else if (a.c == b.c)
	{
		r.c = '1';
		r.sign = !r.sign;
	}
	else if (a.c=='i' && b.c=='j')
	{
		r.c = 'k';
	}
	else if (a.c=='i' && b.c=='k')
	{
		r.c = 'j';
		r.sign = !r.sign;
	}
	else if (a.c=='j' && b.c=='i')
	{
		r.c = 'k';
		r.sign = !r.sign;
	}
	else if (a.c=='j' && b.c=='k')
	{
		r.c = 'i';
	}
	else if (a.c=='k' && b.c=='i')
	{
		r.c = 'j';
	}
	else
	{
		r.c = 'i';
		r.sign = !r.sign;
	}
	return r;
}

const int sz = 44;
vector<quat> aa(sz, quat());

quat xaa(long long x)
{
	quat r;
	for (int i = sz-2; i>=0; --i)
	{
		if ((x & (1L<<i)) > 0)
		{
			r = multiple(r, aa[i+1]);
		}
	}
	return r;
}

string dijkstra(string s, int L, long long X)
{
	quat tmp;
	vector<quat> lprod(L, tmp), rprod(L, tmp);
	lprod[0].c = s[0];
	for (int i = 1; i < L; ++i)
	{
		tmp.c = s[i];
		lprod[i] = multiple(lprod[i-1], tmp);
	}
	rprod[L-1].c = s[L-1];
	for (int i = L-2; i>=0; --i)
	{
		tmp.c = s[i];
		rprod[i] = multiple(tmp, rprod[i+1]);
	}

	aa[0].c = '1';
	aa[1] = rprod[0];
	for (int i = 2; i < sz; ++i)
	{
		aa[i] = multiple(aa[i-1], aa[i-1]);
	}

	quat p;
	long long posk = L*X;
	bool flag = false;
	for (long long x = 0L; x < X; ++x)
	{
		for (int i = L-1; i >= 0; --i)
		{
			tmp = multiple(rprod[i], p);
			if (tmp.c=='k' && tmp.sign)
			{
				flag = true;
				break;
			}
			--posk;
		}
		if (flag) break;
		p = multiple(rprod[0], p);
	}
	if (!flag) return "NO";

	quat q;
	rprod.push_back(quat());
	for (long long x = 0L; x < X; ++x)
	{
		for (int i = 0; i < L; ++i)
		{
			tmp = multiple(q, lprod[i]);
			if (tmp.c=='i' && tmp.sign)
			{
				tmp = multiple(rprod[i+1], xaa(X-1-x));
				if (tmp.c=='i' && tmp.sign)
				{
					if (x*L+i+1<posk) return "YES";
				}
			}
		}
		q = multiple(q, rprod[0]);
	}

	return "NO";
}

int main(int argc, char* argv[])
{
	ifstream in("C-small-attempt0.in");
	ofstream out("result.txt");
	int T, L;
	long long X;
	string s;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> L >> X >> s;
		out << "Case #" << i+1 << ": " << dijkstra(s, L, X) << endl;
	}

	in.close();
	out.close();
	return 0;
}