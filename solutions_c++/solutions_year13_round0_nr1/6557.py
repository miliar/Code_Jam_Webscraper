/*
 this code was written by Zanaty
 problem kind:
 */
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<set> 
#include<cmath>
#include<fstream>
#include<memory.h>
#include<map>
#include<sstream>
#include<climits>
#include<numeric>/*
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
*/
using namespace std;

#define rep(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define reps(i,x,n) for((i)=(x);(i)<(int)(n);(i)++)
#define repi(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define SZ(v) (int)v.size()
#define LEN(s) (int)s.length()
#define mp(x,y) make_pair(x,y)
#define ll long long
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define vi vector<int>
#define vvi vector<vi>

#define INF (int)10e8
#define MAX (int) 1000

char grid[5][5];

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.txt", "r", stdin);
	freopen("out.txt","w",stdout);
#endif

	int test, tt = 1;
	scanf("%d", &test);

	int x = 0, y = 0, t = 0;
	while (test--) {
		int i, j;
		rep(i,4)
			scanf("%s", grid[i]);

		int count = 0;

		// rows

		rep(i,4) {
			x = 0, y = 0, t = 0;
			rep(j,4) {
				if (grid[i][j] == 'X')
					x++;
				else if (grid[i][j] == 'O')
					y++;
				else if (grid[i][j] == 'T')
					t++;
				else
					count++;
			}
			if (x == 4 || (x == 3 && t == 1))
				goto xwin;
			if (y == 4 || (y == 3 && t == 1))
				goto ywin;
		}

		// cols

		rep(j,4) {
			x = 0, y = 0, t = 0;
			rep(i,4) {
				if (grid[i][j] == 'X')
					x++;
				else if (grid[i][j] == 'O')
					y++;
				else if (grid[i][j] == 'T')
					t++;
			}
			if (x == 4 || (x == 3 && t == 1))
				goto xwin;
			if (y == 4 || (y == 3 && t == 1))
				goto ywin;
		}
		x = 0, y = 0, t = 0;

		// diag -1
		rep(i,4) {
			if (grid[i][3 - i] == 'X')
				x++;
			else if (grid[i][3 - i] == 'O')
				y++;
			else if (grid[i][3 - i] == 'T')
				t++;
		}
		if (x == 4 || (x == 3 && t == 1))
			goto xwin;
		if (y == 4 || (y == 3 && t == 1))
			goto ywin;

		x = 0, y = 0, t = 0;
		rep(i,4) {
			if (grid[3 - i][3 - i] == 'X')
				x++;
			else if (grid[3 - i][3 - i] == 'O')
				y++;
			else if (grid[3 - i][3 - i] == 'T')
				t++;
		}
		if (x == 4 || (x == 3 && t == 1))
			goto xwin;
		if (y == 4 || (y == 3 && t == 1))
			goto ywin;

		if (!count)
			goto draw;

		printf("Case #%d: Game has not completed\n", tt++);
		continue;

		xwin: printf("Case #%d: X won\n", tt++);
		continue;
		ywin: printf("Case #%d: O won\n", tt++);
		continue;
		draw: printf("Case #%d: Draw\n", tt++);

	}

	return 0;
}
