#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(v) v.begin(), v.end()

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int tt, n;
	cin >> tt;
	string s;
	forn(tc, tt) {
		cin >> n >> s;
		++n;
		int res = 0, c = 0;
		forn(i, n) {
			if (s[i] > '0' && c < i) {
				res += i - c;
				c = i;
			}
			c += s[i] - '0';
		}
		printf("Case #%d: %d\n", tc+1, res);
	}
}