#include <cstdio>
#include <cstring>
using namespace std;

int t, ans, cnt[20], a, res, ile;

int main() {
	scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		memset(cnt, 0, sizeof(cnt));
		for(int q = 0; q < 2; q++) {
			scanf("%d", &ans);
			for(int i = 1; i <= 4; i++) {
				for(int j = 1; j <= 4; j++) {
					scanf("%d", &a);
					if(i==ans)
						cnt[a]++;
				}
			}
		}
		ile = 0;
		for(int i = 1; i <= 16; i++) {
			if(cnt[i]==2) {
				res = i;
				ile++;
			}
		}
		if(ile==0)
			printf("Case #%d: Volunteer cheated!\n", c);
		if(ile==1)
			printf("Case #%d: %d\n", c, res);
		if(ile>1)
			printf("Case #%d: Bad magician!\n", c);
	}
	return 0;
}
