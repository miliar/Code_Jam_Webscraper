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
//const int inf = 0x7fffffff;
typedef long long int llint;
const double eps = 1e-10;
const double inf = 1e+308;
const llint mod = 1000000007;

char car[101][101];
int len[101];
char buf[10200]; // 100*100

int seen[256];

bool check_valid(char* str)
{
	memset(seen, 0, sizeof seen);
	int last = -1;
	for (char* p = str; *p; p++) {
		if (seen[*p] == 0) {
			seen[*p] = 1;
			last = *p;
		}
		else {
			if (last != *p) return false;
		}
	}
	return true;
}

void solve()
{
	int i, j, k, pos;
	int perm[] = {0,1,2,3,4,5,6,7,8,9,10,11};
	int n;
	int sol = 0;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s", car[i]);
		len[i] = strlen(car[i]);
	}

	do {
		pos = 0;
		for (i = 0; i < n; i++) {
			j = perm[i];
			memcpy(buf+pos, car[j], len[j]);
			pos += len[j];
		}
		buf[pos] = 0;
		if (check_valid(buf)) sol++;
	} while (next_permutation(perm, perm+n));

	printf("%d\n", sol);
}


int main()
{
	int t, i;
	
	scanf("%d", &t);
	
	for (i = 0; i < t; i++) {
		fprintf(stderr, "Case #%d: ", i+1);
		printf("Case #%d: ", i+1);
		solve();
	}
	
	return 0;
}
