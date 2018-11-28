#include <cstdio>
#include <iostream>
using namespace std;
char s[101];

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t){
		int sm;
		scanf("%d ", &sm);
		scanf("%s", s);
		int au = s[0] - '0', ans = 0;
		for (int i = 1; i <= sm; ++i){
			int tmp = s[i] - '0';
			if (tmp){
				if (au >= i) {
					au += tmp;
				}
				else {
					ans += i - au;
					au += ans + tmp;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}