#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;

char bd[111][111];
bool closed[111];
bool flowing[111];
int lu[111],ld[111],ll[111],lr[111];

int main() {
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++) {
		int r,c;
		scanf("%d%d", &r, &c);
		REP(i, r) scanf("%s", bd[i]);
		int ans = 0;
		REP(i, 111) ld[i] = lu[i] = ll[i] = lr[i] = -1;
		REP(i, c) closed[i] = flowing[i] = false;
		REP(i, c) {
			REP(j, r) if(bd[j][i] != '.') {
				if(lu[i] == -1)
					lu[i] = j;
				ld[i] = j;
			}
		}
		REP(i, r) {
			REP(j, c) if(bd[i][j] != '.') {
				if(ll[i] == -1)
					ll[i] = j;
				lr[i] = j;
			}
		}
		REP(i, r) REP(j, c) {
			if(lu[j] == i && ld[j] == i && ll[i] == j && lr[i] == j) {
				 i = j = 111;
				 ans = 1<<30;
				 break;
			}
			if((lu[j] == i && bd[i][j] == '^')
			|| (ld[j] == i && bd[i][j] == 'v')
			|| (ll[i] == j && bd[i][j] == '<')
			|| (lr[i] == j && bd[i][j] == '>')
				) {
				ans++;
			}
		}
		/*
		for(int i = 0; i < r; i++) {
			int lft = 0, rgt = c-1;
			while(lft < c && bd[i][lft] == '.') lft++;
			while(rgt >= 0 && bd[i][rgt] == '.') rgt--;
			if(lft == c) {
				continue;
			}
			if(lft == rgt) {
				if(bd[i][lft] != 'v')
					ans++;
				if(closed[lft]) {
					bd[i][lft] = '^';
					flowing[lft] = false;
				} else {
					bd[i][lft] = 'v';
					closed[lft] = true;
					flowing[lft] = true;
				}
			} else {
				if(bd[i][lft] != '>') {
					if((bd[i][lft] == '^' && !closed[lft]) || bd[i][lft] == '<' || (bd[i][lft] == 'v' && last[lft] == i))
						bd[i][lft] = '>';
					closed[lft] = true;
					flowing[lft] = false;
					ans++;
				}
				if(bd[i][rgt] == '>') {
					bd[i][rgt] = '<';
					flowing[rgt] = false;
					closed[rgt] = true;
					ans++;
				}
			}
			for(int j = lft+1; j < rgt; j++) {
				if(bd[i][j] == '^' && !closed[j]) {
					ans++;
					bd[i][j] = '>';
					closed[j] = true;
					flowing[j] = false;					
				}
			}
		}
		bool ok = true;
		for(int i = 0; i < c; i++) {
			if(bd[r-1][i] == 'v' && !closed[i])
				ok = false;
			if(flowing[i])
				ok = false;
			 
		}*/
		if(ans == 1<<30)
			printf("Case #%d: IMPOSSIBLE\n", testc);
		else
			printf("Case #%d: %d\n", testc, ans);

	}
	return 0;
}
