/*
ID: eoart2
PROG: transform
LANG: C++
*/
//#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:134217728")
#include <cstdio>
#include <iostream>
#include <iomanip> 
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <string>
#include <functional>
#include <cassert>
#include <random>

const long long MOD = 1000000007;
const int INF = 2000000000;
const int MAXN = 200000;
const double EPS = 1e-9;
const int HASH_POW = 7;
const double PI = acos(-1.0);

using namespace std;

void my_return(int code)
{
#ifdef MYDEBUG
	cout << "\nTime = " << fixed << setprecision(3) << double(clock()) / CLOCKS_PER_SEC << endl;
#endif
	exit(code);
}

int main()
{
	//cin.sync_with_stdio(0);
	mt19937 mt_rand(time(NULL));
	#ifdef MYDEBUG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	#else
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	#endif

	int CASE;
	cin >> CASE;
	for (int T = 1; T <= 25; ++T)
	{
		int n;
		cin >> n;
		map <string, int> msk;
		string s;
		getline(cin, s);
		for (int i = 0; i < n; ++i)
		{
			getline(cin, s);
			while (s.find(' ') != -1)
			{
				int x = s.find(' ');
				string tmp = s.substr(0, x);
				s.erase(0, x + 1);
				msk[tmp] |= (1 << i);
			}
			msk[s] |= (1 << i);
		}
		
		int cnt = 0, finalans = 100000;
		for (int i = 0; i < (1 << n); ++i)
		{
			if ((i & 1) == 1 || (i & 2) == 0)
				continue;

			cnt = 0;
			for (map <string, int>::iterator it = msk.begin(); it != msk.end(); ++it)
			{
				int s1 = it->second, s2 = i;
				if ((s1 & s2) != 0 && (s1 & s2) != s1)
					++cnt;
			}
			finalans = min(finalans, cnt);
		}

		cout << "Case #" << T << ": " << finalans << "\n";
	}

	my_return(0);
}