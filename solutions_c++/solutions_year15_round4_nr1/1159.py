#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define EPS 1E-9
#define INF 2000000000
#define ll long long
#define ld long double
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define MAXN 100001


string s[123];
int n, m;

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		printf("Case #%d: ", ttt + 1);
		cin >> n >> m;
		forn(i, n)
			cin >> s[i];

		int res = 0;
		// check IMPOSSIBLE
		int ok = 1;
		forn(i, n)
			forn(j, m) {
				if (s[i][j] == '.')continue;
				if (!ok)
					break;
				int save = 0;
				forn(k, n)
					if (k != i && s[k][j] != '.') {
						save = 1;
						break;
					}
				forn(k, m)
					if (k != j && s[i][k] != '.') {
						save = 1;
						break;
					}
				if (!save)
					ok = 0;
			}
		if (!ok) {
			puts("IMPOSSIBLE");
			continue;
		}

		forn(i, n) {
			forn(j, m) {
				if (s[i][j] == '.')
					continue;
				if (s[i][j] == '<') {
					// check left
					bool ok = 0;
					forn(k, j)
						if (s[i][k] != '.') {
							ok = 1;
							break;
						}
					if (ok)
						continue;
					++res;
					continue;
				}
				if (s[i][j] == '^') {
					// check top
					bool ok = 0;
					forn(k, i)
						if (s[k][j] != '.') {
							ok = 1;
							break;
						}
					if (ok)
						continue;
					++res;
					continue;
				}
				if (s[i][j] == '>') {
					// check right
					bool ok = 0;
					fore(k, j + 1, m)
						if (s[i][k] != '.') {
							ok = 1;
							break;
						}
					if (ok)
						continue;
					++res;
					continue;
				}
				if (s[i][j] == 'v') {
					bool ok = 0;
					fore(k, i + 1, n) {
						if (s[k][j] != '.') {
							ok = 1;
							break;
						}
					}
					if (ok)
						continue;
					++res;
					continue;
				}
			}
		}
		cout << res << endl;
		/*
		forn(i, n) {
			int leftmost = -1;
			forn(j, m) {
				if (s[i][j] != '.') {
					if (s[i][j] == '<' && !used[i][j]) {
						used[i][j] = 1;
						res++;
					}
					leftmost = j;
					break;
				}
			}
			int rightmost = -1;
			for(int j = m - 1; j >= 0; --j) {
				if (s[i][j] != '.') {
					if (s[i][j] == '>' && !used[i][j]) {
						used[i][j] = 1;
						res++;
					}
					rightmost = j;
					break;
				}
			}
		}
		*/
				
	}
}