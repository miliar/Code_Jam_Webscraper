//#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
//#define TASK "A-small-attempt0"
#define TASK "A-large"
#pragma comment(linker, "/STACK:536870912")
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
#include <map>
#include <string>
#include <functional>
#include <cassert>
#include <bitset>
#include <unordered_set>
#include <unordered_map>
#include <random>

const int MOD = 1000000003;
const int INF = 1000000001;
const int MAXN = 100000;
const long double EPS = 1e-8;
const int HASH_POW = 29;
const long double PI = acos(-1.0);

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
	cin.sync_with_stdio(0);
	cin.tie(0);
	mt19937 mt_rand(time(0));
#ifdef MYDEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen(TASK".in", "rt", stdin);
	freopen(TASK".out", "wt", stdout);
	/*freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);*/
#endif

	int CASE;
	cin >> CASE;
	for (int it = 1; it <= CASE; ++it)
	{
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		vector <string> r0, p0, s0, r1, p1, s1;
		for (int i = 0; i < r; ++i)
			r0.push_back("R");
		for (int i = 0; i < p; ++i)
			p0.push_back("P");
		for (int i = 0; i < s; ++i)
			s0.push_back("S");

		bool good = true;
		for (int timer = 0; timer < n; ++timer)
		{
			int sizer1 = ((int)r0.size() - (int)p0.size() + (int)s0.size()) / 2;
			int sizep1 = ((int)r0.size() + (int)p0.size() - (int)s0.size()) / 2;
			int sizes1 = (-(int)r0.size() + (int)p0.size() + (int)s0.size()) / 2;
			if (sizer1 < 0 || sizep1 < 0 || sizes1 < 0)
			{
				good = false;
				break;
			}
			for (int i = 0; i < sizer1; ++i)
			{
				string tmp1 = r0.back(), tmp2 = s0.back();
				r0.pop_back();
				s0.pop_back();
				if (tmp1 < tmp2)
					r1.push_back(tmp1 + tmp2);
				else
					r1.push_back(tmp2 + tmp1);
			}
			for (int i = 0; i < sizep1; ++i)
			{
				string tmp1 = p0.back(), tmp2 = r0.back();
				p0.pop_back();
				r0.pop_back();
				if (tmp1 < tmp2)
					p1.push_back(tmp1 + tmp2);
				else
					p1.push_back(tmp2 + tmp1);
			}
			for (int i = 0; i < sizes1; ++i)
			{
				string tmp1 = s0.back(), tmp2 = p0.back();
				s0.pop_back();
				p0.pop_back();
				if (tmp1 < tmp2)
					s1.push_back(tmp1 + tmp2);
				else
					s1.push_back(tmp2 + tmp1);
			}
			r0 = r1;
			r1.clear();
			p0 = p1;
			p1.clear();
			s0 = s1;
			s1.clear();
		}

		cout << "Case #" << it << ": ";
		if (good)
		{
			if (!r0.empty())
				cout << r0[0] << endl;
			else if (!p0.empty())
				cout << p0[0] << endl;
			else
				cout << s0[0] << endl;
		}
		else
			cout << "IMPOSSIBLE\n";
	}

	my_return(0);
}