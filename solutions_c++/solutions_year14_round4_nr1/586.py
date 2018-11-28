#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 100001
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define mp make_pair


int a[12345];
void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int ttt;
	scanf("%d", &ttt);
	forn(tt, ttt) {
		int x, n;
		
		scanf("%d %d", &n, &x);
		forn(i, n)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int j = 0, i = n - 1, res = 0;
		while(j <= i) {
			if (i == j){
				++res;
				break;
			}
			if (a[i] + a[j] > x) {
				--i, ++res;
			} else {
				++j, --i, ++res;
			}
		}
		printf("Case #%d: %d\n", tt + 1, res);
	}
}