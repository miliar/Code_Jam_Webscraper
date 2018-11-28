	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

string c, j, bestC, bestJ;
int n;

unsigned long long get(string s)
{
	unsigned long long res = 0;
	for(int i = 0; i < n; i++)
		res = res * 10 + s[i] - '0';
	return res;
}

void work(string a, string b)
{
	unsigned long long A = get(a), B = get(b);
	if(bestC.empty())
	{
		bestC = a;
		bestJ = b;
		return;
	}
	unsigned long long lA = get(bestC), lB = get(bestJ);
	unsigned long long diff = (A >= B ? A - B : B - A);
	unsigned long long ldiff = (lA >= lB ? lA - lB : lB - lA);
	if(diff < ldiff)
	{
		bestC = a;
		bestJ = b;
		return;
	}
	if(diff > ldiff)
		return;
	if(A < lA)
	{
		bestC = a;
		bestJ = b;
		return;
	}
	if(A > lA)
		return;
	if(B < lB)
	{
		bestC = a;
		bestJ = b;
		return;
	}
}

int main()
{
	int tests = in();
	for(int _t = 1; _t <= tests; _t++)
	{
		cout << "Case #" << _t << ": ";
		cin >> c >> j;
		bestC = bestJ = string();
		n = c.size();
		c += '?';
		j += '?';
		for(int firstDiff = 0; firstDiff <= n; firstDiff++)
		{
			for(int cD = 0; cD < 10; cD++)
				for(int jD = 0; jD < 10; jD++)
					if(c[firstDiff] == '?' || c[firstDiff] == cD + '0')
						if(j[firstDiff] == '?' || j[firstDiff] == jD + '0')
						{
							if(cD == jD)
								continue;
							string cc = c, jj = j;
							bool bad = 0;
							for(int i = 0; i < firstDiff; i++)
								if(c[i] != '?')
									if(j[i] == '?')
										jj[i] = c[i];
									else
										bad |= (j[i] != c[i]);
								else if(j[i] != '?')
									cc[i] = j[i];
								else
									cc[i] = jj[i] = '0';
							if(bad)
								continue;
							if(firstDiff == n)
							{
								work(cc, jj);
								continue;
							}
							cc[firstDiff] = cD + '0';
							jj[firstDiff] = jD + '0';
							int ccD = 0, jjD = 0;
							if(cD < jD)
								ccD = 9;
							else
								jjD = 9;
							for(int i = firstDiff + 1; i < n; i++)
							{
								if(cc[i] == '?')
									cc[i] = ccD + '0';
								if(jj[i] == '?')
									jj[i] = jjD + '0';
							}
							work(cc, jj);
						}
		}
		bestC.pop_back();
		bestJ.pop_back();
		cout << bestC << " " << bestJ << endl;
	}
}
