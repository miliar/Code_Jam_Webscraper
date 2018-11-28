#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <climits>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define REP1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define wait system("pause")

int main()
{
	ifstream in("B-small-attempt0(1).in");
	ofstream out("B.out");
	int T;
	in >> T;
	REP1(II, T)
	{
		out << "Case #" << II << ": ";
		int a, b, k;
		ll ans = 0;
		in >> a >> b >> k;
		REP(i,a)
			REP(j, b)
		{
				int t = i & j;
				if (t < k)
					ans++;
		}
		out << ans;
		out << "\n";
	}
	in.close();
	out.close();
	return 0;
}