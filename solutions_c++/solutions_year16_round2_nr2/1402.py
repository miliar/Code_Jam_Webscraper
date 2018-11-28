#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
#include <bitset>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(ll i = 0; i<(int)N; i++)
#define fornj(N)         for(ll j = 0; j<(int)N; j++)
#define fornk(N)         for(ll k = 0; k<(int)N; k++)
#define forn1(N)          for(ll i = 1; i<=(int)N; i++)
#define fornj1(N)         for(ll j = 1; j<=(int)N; j++)
#define fornk1(N)         for(ll k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define v vector
#define File "fileName"

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

#define log2BitApproximate(S) ((int)(log((double)S) / log(2.0)))
#define log2Bit(S) (1 << (log2BitApproximate(S) + 1) > S ? log2BitApproximate(S) : log2BitApproximate(S) + 1)
#define highBit(S) (isPowerOfTwo(S) ? S : 1 << log2Bit(S))

#define modulo(S, N) ((S) & (N - 1))   // returns S % N, where N is a power of 2
#define isPowerOfTwo(S) (!(S & (S - 1)))
#define nearestPowerOfTwo(S) ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define turnOffLastBit(S) ((S) & (S - 1))
#define turnOnLastZero(S) ((S) | (S + 1))
#define turnOffLastConsecutiveBits(S) ((S) & (S + 1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S - 1))

using namespace std;

const ll MOD = 1000000007;

void decrease(v<int>& freq, string s, int n)
{
	forn(n)
	{
		fornj(s.length())
		{
			freq[s[j] - 'A']--;
		}
	}
}

v<string> fP;
v<string> fS;

void tryOut(string s, int i, vector<string>& w)
{
	if (i >= s.length())
	{
		w.push_back(s);
	} else
	{
		if (s[i] == '?')
		{
			for (char c = '0'; c <= '9'; ++c)
			{
				s[i] = c;
				tryOut(s, i + 1, w);
			}
		}
		else tryOut(s, i + 1, w);
	}
		

}

int myAb(int a)
{
	return a < 0 ? -a : a;
}

int diff(string s, string t)
{
	stringstream s1, s2;
	s1 << s;
	s2 << t;
	int a = atoi(s1.str().c_str());
	int b = atoi(s2.str().c_str());

	return myAb(a - b);
	
}

int main()

{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int t;
	cin >> t;
	forn(t)
	{
		string c,jj;
		cin >> c >> jj;
		

		bool eq = true;
		bool f = true;

		fP.clear();
		fS.clear();

		tryOut(c, 0, fP);
		tryOut(jj, 0, fS);
		
		
		int minD = INT_MAX;
		string s1, s2;
		fornj(fP.size())
		{
			fornk(fS.size())
			{
				int pos = diff(fP[j], fS[k]);
				if (pos < minD)
				{
					minD = pos;
					s1 = fP[j];
					s2 = fS[k];
				} else if (pos == minD)
				{
					if (fP[j] < s1 || (fP[j] == s1 && fS[k] < s2))
					{
						s1 = fP[j];
						s2 = fS[k];
					}
				}
			}
		}

		//if (i % 10 == 0) cout << i << endl;
		/*fornj(c.size())
		{
			if (jj[j] != '?' && c[j] == '?')
			{
				if (eq)
					c[j] = jj[j];
				else
				{
					if (f)
					{
						c[j] = '0';
					}
					else
					{
						c[j] = '9';
					}
				}
			}
			else if (jj[j] == '?' && c[j] != '?')
			{
				if (eq)
				jj[j] = c[j];
				else
				{
					if (f)
					{
						jj[j] = '9';
					}
					else
					{
						
						jj[j] = '0';
					}
				}
			} else if (jj[j] == '?' && c[j] == '?')
			{
				if (eq)
				{
					c[j] = '0';
					jj[j] = '0';
				}
				else
				{
					if (f)
					{
						c[j] = '0';
						jj[j] = '9';
					}
					else
					{
						c[j] = '9';
						jj[j] = '0';
					}
				}
			}else
			{
				if (c[j] > jj[j])
				{
					eq = false;
					f = true;
				} else if (jj[j] > c[j])
				{
					eq = false;
					f = false;
				}
			}

		}
*/
		cout << "Case #" << i + 1 << ": " << s1 << " " << s2 << endl;
	}

	return 0;
}