#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

#define Fr(a,b,c) for(int a = b; a < c; ++a)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oo 0x3F3F3F3F

#define dbg if(0)

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long rash;

int inix[] = {0, 0, 0, 0,   0,  0,   0, 1, 2, 3 };
int iniy[] = {0, 1, 2, 3,   0,  3,   0, 0, 0, 0 };
int incx[] = {1, 1, 1, 1,   1,  1,   0, 0, 0, 0 };
int incy[] = {0, 0, 0, 0,   1, -1,   1, 1, 1, 1 };

#define valid(x,y) (0 <= x && x < 4 && 0 <= y && y < 4)

char inp[10][10];

int n;
int main() {
	int t, caso = 0; scanf("%d", &t);
	while(t--) {
		Fr(i,0,4) scanf("%s", inp[i]);

		bool empty = false;
		bool oWin = false, xWin = false;
		Fr(i,0,4) Fr(j,0,4) empty |= inp[i][j] == '.';
		
		// 'O' win ?
		Fr(k,0,10) {
			int a = inix[k], b = iniy[k];
			bool ok = true;
			Fr(j,0,4) {
//				assert(valid(a,b));
				ok &= inp[a][b] == 'O' || inp[a][b] == 'T';
				a += incx[k], b += incy[k];
			}
			if(ok) oWin = true;
		}
		
		// 'X' win ?
		Fr(k,0,10) {
			int a = inix[k], b = iniy[k];
			bool ok = true;
			Fr(j,0,4) {
//				assert(valid(a,b));
				ok &= inp[a][b] == 'X' || inp[a][b] == 'T';
				a += incx[k], b += incy[k];
			}
			if(ok) xWin = true;
		}
		
		if(xWin) printf("Case #%d: X won\n", ++caso);
		else if(oWin) printf("Case #%d: O won\n", ++caso);
		else if(empty) printf("Case #%d: Game has not completed\n", ++caso);
		else printf("Case #%d: Draw\n", ++caso);
	}
	
	return 0;
}


