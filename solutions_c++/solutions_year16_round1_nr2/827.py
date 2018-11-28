#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair


#define MAXN 105
vector<int> A[MAXN];
int grid[MAXN][MAXN];
bool seen_col[MAXN];

int main() {
	int TEST;
	int N,x;

	scanf("%d",&TEST);
	FOR(test,TEST) {
		memset(grid,0,sizeof(grid));
		memset(seen_col,0,sizeof(seen_col));
		scanf("%d",&N);
		FOR(i,2*N-1) A[i].clear();

		FOR(i,2*N-1) FOR(j,N) scanf("%d",&x), A[i].pb(x);
		sort(A,A+(2*N-1));

		int numS = (1<<(2*N-1));
		FOR(s,numS) {
			if (__builtin_popcount(s) != N) continue;
			memset(seen_col, 0, sizeof(seen_col));

			int row = 0;
			FOR(i,2*N-1) {
				if (s & (1<<i)) {
					FOR(col,N) grid[row][col] = A[i][col];
					row++;
				}
			}

			bool works = true;
			FOR(i,N) FOR(j,N) {
				if (i>0 && grid[i][j] <= grid[i-1][j]) works = false;
				if (j>0 && grid[i][j] <= grid[i][j-1]) works = false;
			}


			if (!works) continue;

			FOR(i,2*N-1) {
				if (s&(1<<i)) continue;
				bool found_one = false;
				FOR(col,N) {
					if (seen_col[col]) continue;
					bool matches = true;
					FOR(row,N) if (grid[row][col] != A[i][row]) matches = false;
					if (matches) {
						seen_col[col] = true;
						found_one = true;
						break;
					}
				}
				if (!found_one) works = false;
			}

			if (!works) continue;
			printf("Case #%d:", test+1);

			int best_col = -1;
			FOR(col,N) if (!seen_col[col]) best_col = col;
			FOR(row,N) printf(" %d", grid[row][best_col]);
			printf("\n");
			break;
		}
	}
    
}































