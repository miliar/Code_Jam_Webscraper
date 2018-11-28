// Wsl_F

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>
// Wsl_F

using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))

const int MaxN = 26;

int p[MaxN + 5];

struct classCmp
{
	bool operator() (const pii &l, const  pii &r) const
	{
		return l.first > r.first || (l.first == r.first && l.second > r.second);
	}
};

void solve()
{
	int n;
	cin >> n;

	set<pii, classCmp> s;
	for (int i = 0; i < n; i++)
	{
		cin >> p[i];
		s.insert(mp(p[i], i));
	}

	while (!s.empty())
	{
		pii first = *s.begin();
		s.erase(s.begin());
		pii second = *s.begin();
		s.erase(s.begin());
		if (s.empty())
		{
			for (int i = 0; i < first.first; i++)
			{
				cout << (char)('A' + first.second) << (char)('A' + second.second) << " ";
			}
			cout << endl;
			return;
		}

		cout << (char)('A' + first.second);
		first.first--;
		if ((*s.begin()).first < second.first)
		{
			cout << (char) ('A' + second.second);
			second.first--;
		}

		cout << " ";
		if (first.first > 0)
			s.insert(first);
		if (second.first > 0)
			s.insert(second);
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	srand(__rdtsc());

	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-output.txt","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large-output.txt","w",stdout);
	//cout<<fixed;
	//cout<<setprecision(9);

	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		cout << "Case #" << testCase << ": ";
		solve();
	}


	return 0;
}
