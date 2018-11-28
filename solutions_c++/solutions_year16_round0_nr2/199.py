#include <cstdio>

const int MAXN = 1E2 + 10;

char s[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);
		
		scanf("%s", s);
		int i = 1, cnt = 1;
		for (; s[i]; ++i)
			cnt += s[i] != s[i - 1];
		cnt -= s[i - 1] == '+';
		printf("%d\n", cnt);
	}
	return 0;
}
