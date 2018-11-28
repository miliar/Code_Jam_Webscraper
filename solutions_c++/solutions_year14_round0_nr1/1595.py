#include <cstdio>
#include <algorithm>

using namespace std;

bool rep[17];

int main(){
	int T, cas, i, target, a, ans;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++){
		fill_n(rep, 17, 0);
		ans = 0;
		scanf("%d", &target);
		for (i = 0; i < 16; i++){
			scanf("%d", &a);
			if (i/4+1 == target) rep[a] = 1;
		}
		scanf("%d", &target);
		for (i = 0; i < 16; i++){
			scanf("%d", &a);
			if (i/4+1 == target && rep[a]){
				if (!ans) ans = a;
				else ans = -1;
			}
		}
		printf("Case #%d: ", cas);
		if (!ans) printf("Volunteer cheated!\n");
		else if (ans < 0) printf("Bad magician!\n");
		else printf("%d\n", ans);
	}
}

