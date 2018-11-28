#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n;
double naomi[1010], ken[1010];

int main() {
	int t; scanf("%d",&t);
	for(int k = 0; k < t; ++k) {
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%lf", &naomi[i]);
		for(int i = 0; i < n; ++i)
			scanf("%lf", &ken[i]);
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		int dwar = 0, war = 0;
		for(int i = 0, j = 0; i < n; ++i)
			if(naomi[i] > ken[j])
				++j, ++dwar;
		for(int i = n - 1, j = n - 1; i >= 0; --i) {
			if(naomi[i] > ken[j]) ++war;
			else --j;
		}
		printf("Case #%d: %d %d\n", k + 1, dwar, war);
	}
	return 0;
}
