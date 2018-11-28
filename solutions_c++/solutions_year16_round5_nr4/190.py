#include <cstdio>
#include <cstring>
using namespace std;
#define N 222
int n, L;
char ch[N];

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int _, __ = 0;
	scanf("%d", &_);
	while (_--){
		printf("Case #%d: ", ++ __);
		scanf("%d%d", &n, &L);
		int ans = 1;
		for (int i = 0; i < n; ++ i){
			scanf("%s", ch);
			int flag = 0;
			for (int j = 0; j < L; ++ j){
				if (ch[j] == '0'){
					flag = 1;
				}
			}
			if (flag == 0){
				ans = 0;
			}
		}
		scanf("%s", ch);
		if (ans == 0){
			puts("IMPOSSIBLE");
			continue;
		}
		for (int i = 0; i < L - 1; ++ i){
			printf("?");
		}
		if (L == 1){
			printf("0");
		}
		printf(" ");
		for (int i = 0; i < (196 - L + 1) / 2; ++ i){
			printf("10");
		}
		printf("?1\n");
	}
	return 0;
}