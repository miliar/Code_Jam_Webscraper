#include <cstdio>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	char str[1004], ans[2004];
	for(int NOWCASE=1; NOWCASE<=T; ++NOWCASE) {
		scanf("%s", str);
		int f = 1001, e=1003;
		ans[1002] = str[0];
		for(int i=1; str[i]!='\0'; ++i) {
			if( str[i]>=ans[f+1] ) {
				ans[f] = str[i];
				--f;
			}
			else {
				ans[e] = str[i];
				++e;
			}
		}
		ans[e] = '\0';
		printf("Case #%d: %s\n", NOWCASE, ans+f+1);
	}
	return 0;
}
