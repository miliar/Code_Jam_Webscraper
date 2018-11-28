#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <functional>
#include <string>
#include <algorithm>

#include <cstring>
#include <cstdio>
#include <memory.h>
#include <ctime>
#include <cassert>
#include <cmath>
using namespace std;

//#pragma comment(linker, "/STACK:66777216")

#define forn(i,n) for(int i = 0; i < int(n); i++)
#define ford(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define fore(i,a,b) for(int i = int(a); i <= int(b); i++)
#define foreach(it,a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)

#define mp make_pair
#define pb push_back
#define L(s) ((int)((s).size()))
#define sq(x) ((x)*(x))
#define sign(x) ( ((x) > 0) ? 1 : -1)

#define ll long long
#define INF 1000000000
#define eps e-8

void solveA()
{
	int T;
	cin >> T;
	forn(t, T)
	{
		string s;
		cin >> s;
		ll p, q;
		int sn = s.size();
		forn(i, sn)
		{
			if (s[i] == '/')
			{
				string s1 = s.substr(0, i);
				istringstream ss(s1);
				ss >> p;
				string s2 = s.substr(i + 1, sn - i - 1);
				istringstream ss2(s2);
				ss2 >> q;
				break;
			}
		}
		bool ok = false;
		int res=0;
		if (p < q)
		{
			ll qc = q;
			for (ll j = 2; j*j <= qc; ++j)
			{
				while(p%j == 0 && q%j == 0)
				{
					p /= j;
					q /= j;
				}
			}
			int mpt = 0;
			ll cur = 1;
			while (mpt <= 40 && q != cur)
			{
				mpt++;
				cur *= 2;
			}
			if (mpt <= 40)
			{
				int tp = 0;
				cur = 2;
				while (p >= cur)
				{
					tp++;
					cur *= 2;
				}
				ok = true;
				res = mpt - tp;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if (ok)
			cout << res << endl;
		else
			cout << "impossible" << endl;
	}
}

int main() {

#ifdef diametralis
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	solveA();

#ifdef diametralis
	cerr << "Time == " << clock() << endl;
#endif
}