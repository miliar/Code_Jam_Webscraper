#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define EPS 1e-10
const double PI = acos(-1.0);

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

///////////////////////////////////////////////////////////////////////////////////////////////////////


int a[200][200];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	for(int tc=1; tc<=T; tc++) {
		printf("Case #%d: ", tc);

		int m, n;
		scanf("%d %d", &m, &n);

		for(int i=0; i<m; i++) {
			for(int j=0; j<n; j++) {
				scanf("%d", &a[i][j]);
			}
		}

		bool poss(true);
		for(int i=0; i<m; i++) {
			for(int j=0; j<n; j++) {
				int cur = a[i][j];
				bool flag0(true);
				for(int i2=0; i2<m; i2++) {
					if(a[i2][j] > cur) {
						flag0 = false;
					}
				}
				bool flag1(true);
				for(int j2=0; j2<n; j2++) {
					if(a[i][j2] > cur) {
						flag1 = false;
					}
				}
				if(!flag0 && !flag1)	poss = false;
			}
		}

		if(poss)	printf("YES\n");
		else	printf("NO\n");



		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}