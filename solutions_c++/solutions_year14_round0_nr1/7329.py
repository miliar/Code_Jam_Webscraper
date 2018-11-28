#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <math.h>

#include <algorithm>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>

#define FOR(var, size) for (int (var) = 0; (var) < (size); (var)++)

using namespace std;
const int inf = 0x7fffffff;
typedef long long int llint;
const double eps = 1e-10;
//const double inf = 1e+309;


void solve()
{
	int m[17] = {0};
	int i, j, k;
	int a, b;
	FOR(k, 2) {
		scanf("%d", &a); a--;
		FOR(i, 4) {
			FOR (j, 4) {
				scanf("%d", &b);
				if (i == a) continue;
				m[b] = 1;
			}
		}
	}
	int cnt = 0, last = 0;
	FOR(i, 16) {
		if (m[i+1] == 0) {
			last = i+1;
			cnt++;
		}
	}
	if (cnt == 0)
		printf("Volunteer cheated!\n");
	else if (cnt > 1)
		printf("Bad magician!\n");
	else
		printf("%d\n", last);
}


int main()
{
	int t, i;
	
	scanf("%d", &t);
	
	for (i = 0; i < t; i++) {
		printf("Case #%d: ", i+1);
		solve();
	}
	
	return 0;
}

