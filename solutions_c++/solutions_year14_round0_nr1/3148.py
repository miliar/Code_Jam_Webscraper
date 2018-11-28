#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 20;

int cnt[N];

int main() {
	int t;
	scanf("%d", &t);

	for(int kase = 0; kase < t; kase++) {
		fill(cnt, cnt + N, 0);

		int x;
		scanf("%d", &x);

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				int tmp;
				scanf("%d", &tmp);
				if(i == x - 1)	cnt[tmp]++;
			}
		}

		int y;
		scanf("%d", &y);

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				int tmp;
				scanf("%d", &tmp);
				if(i == y - 1)	cnt[tmp]++;
			}
		}

		int cnt2 = 0, ans = 0;
		for(int i = 1; i <= 16; i++) {
			if(cnt[i] == 2) {
				cnt2++;
				ans = i;
			}
		}

		printf("Case #%d: ", kase+1);
		if(!cnt2)	puts("Volunteer cheated!");
		else if(cnt2 >= 2)	puts("Bad magician!");
		else	printf("%d\n", ans);
	}

	return 0;
}
