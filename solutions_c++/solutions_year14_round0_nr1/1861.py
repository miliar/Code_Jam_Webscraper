#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

int a[18],n,g[6][6];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++) {
				scanf("%d",&g[i][j]);
				if (i == n-1) a[g[i][j]]++;
			}
		scanf("%d",&n);
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++) {
				scanf("%d",&g[i][j]);
				if (i == n-1) a[g[i][j]]++;
			}

		int ans = -1;
		for (int i=1; i<=16; i++)
			if (a[i] == 2) {
				if (ans != -1) { ans = 1000; break; }
				ans = i;
			}
		if (ans == -1) printf("Case #%d: Volunteer cheated!\n",t);
		else if (ans == 1000) printf("Case #%d: Bad magician!\n",t);
		else printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
