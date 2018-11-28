#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>
using namespace std;

typedef long long ll;

int a[11][11];
int b[111];
int n, m;

int main(){
	int _, cas=0;
	scanf("%d", &_);
	while (_--) {
		memset(b, 0, sizeof(b));
		scanf("%d", &n);
		for (int i=0; i<4; ++i)
			for (int j=0; j<4; ++j)
				scanf("%d", &a[i][j]);
		for (int i=0; i<4; ++i) b[a[n-1][i]] ++;
		
		scanf("%d", &n);
		for (int i=0; i<4; ++i)
			for (int j=0; j<4; ++j)
				scanf("%d", &a[i][j]);
		for (int i=0; i<4; ++i) b[a[n-1][i]] ++;
		int ans = 0, sum = 0;
		for (int i=1; i<=16; ++i)
			if (b[i] == 2) {
				ans = i;
				sum ++;
			}
		if (sum == 0)
			printf("Case #%d: Volunteer cheated!\n", ++cas);
		if (sum == 1)
			printf("Case #%d: %d\n", ++cas, ans);
		if (sum >= 2)
			printf("Case #%d: Bad magician!\n", ++cas);
	}
	return 0;
}