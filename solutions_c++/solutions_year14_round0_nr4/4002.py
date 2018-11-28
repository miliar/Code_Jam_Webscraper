#include <cstdio>
#include <algorithm>

using namespace std;

double me[1024], him[1024];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		int n;
		scanf("%d", &n);

		for(int i = 0; i < n; i++)
			scanf("%lf", &me[i]);
		for(int i = 0; i < n; i++)
			scanf("%lf", &him[i]);

		sort(me, me+n);
		sort(him, him+n);

		int war = 0, deceit = 0;
		int cur = 0;
		for(int i = 0; i < n && cur < n; i++) {
			if(me[i] > him[cur]) { deceit++; cur++; }
		}
		cur = 0;
		for(int i = n-1; i >= 0; i--) {
			if(me[i] > him[i+cur]) { war++; cur++; }
		}

		printf("Case #%d: %d %d\n", t, deceit, war);
	}
	return 0;
}
