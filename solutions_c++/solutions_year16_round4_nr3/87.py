#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define add(x,y) ((ll)(x)+(y))%mod
#define F(i,n) for(int i = 0; i < n; i++)
#define FF(i,n) for(int i = 1; i <= n; i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//

int bd[16][16];
int match[34];

int main() {
#ifndef __GNUG__
	freopen("C-small-attempt0.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: \n", ++casen);
		
		int r, c; nii(r, c);
		int tot = r*c;
		//1:u 2:r 3:d 4:l
		//0:\ 1:/
		int p2 = 1 << tot; 
		F(i, r + c) {
			int x, y; nii(x, y);
			match[x - 1] = y - 1;
			match[y - 1] = x - 1;
		}
		auto func = [&](int start) {
			int dir; pii cell;
			if (start < c) dir = 1, cell = mp(0, start);
			else if (start < r + c) dir = 2, cell = mp(start - c, c - 1);
			else if (start < r + 2 * c) dir = 3, cell = mp(r - 1, c - start + r + c - 1);
			else dir = 4, cell = mp(r - start + r + 2 * c - 1, 0);
			return cell;
		};
		int good = 0;
		F(i, p2) {
			F(j, tot) {
				int x = j / c;
				int y = j%c;
				if (i&(1 << j)) {
					bd[x][y] = 1;
				}
				else bd[x][y] = 0;
			}

			int bad = 0;
			F(start, 2 * (r + c)) {
				int dir; pii cell;
				if (start < c) dir = 1, cell = mp(0, start);
				else if (start < r + c) dir = 2, cell = mp(start - c, c - 1);
				else if (start < r + 2 * c) dir = 3, cell = mp(r - 1, c - start + r + c - 1);
				else dir = 4, cell = mp(r - start + r + 2 * c - 1, 0);
				int dst = match[start];
				auto dest = func(dst);
				if (dst < c) dest.first--;
				else if (dst < r + c) dest.second++;
				else if (dst < r + 2 * c) dest.first++;
				else dest.second--;
				while (cell.first >= 0 && cell.first < r && cell.second >= 0 && cell.second < c) {
					int x = cell.first; int y = cell.second;
					if (!bd[x][y]) {
						if (dir == 1) dir = 4, cell.second++;
						else if (dir == 2) dir = 3, cell.first--;
						else if (dir == 3) dir = 2, cell.second--;
						else dir = 1, cell.first++;
						
					}
					else {
						if (dir == 3) dir =4, cell.second++;
						else if (dir == 4) dir = 3, cell.first--;
						else if (dir == 1) dir = 2, cell.second--;
						else dir = 1, cell.first++;
					}
				}
				if (cell != dest) {
					bad = 1; break;
				}
			}
			if (bad) continue;
			good = 1;
			F(i, r) {
				F(j, c) {
					if (!bd[i][j]) printf("\\");
					else printf("/");
				}
				puts("");
			}

			break;
		}
		if (!good) puts("IMPOSSIBLE");
		
		
		
		fprintf(stderr, "Case %d complete\n", casen);
	}

	return 0;
}
