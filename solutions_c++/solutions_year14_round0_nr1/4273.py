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

int m1[5][5], m2[5][5], f, s;

int main() {
	int t; scanf("%d",&t);
	for(int k = 0; k < t; ++k) {
		scanf("%d", &f);
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				scanf("%d", &m1[i][j]);
		scanf("%d", &s);
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				scanf("%d", &m2[i][j]);
		int cnt = 0, ans;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(m1[f - 1][i] == m2[s - 1][j])
					++cnt, ans = m1[f - 1][i];
		printf("Case #%d: ", k + 1);
		if(!cnt) printf("Volunteer cheated!\n");
		else if(cnt > 1) printf("Bad magician!\n");
		else printf("%d\n", ans);
	}
	return 0;
}

