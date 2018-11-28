#include <cstdio>

const int MAXN = 2E4 + 10;

char s[MAXN];
int tail;
char que[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%s", s);
		int s1 = 0;
		tail = -1;
		for (int i = 0; s[i]; ++i)
			if (tail >= 0 && que[tail] == s[i])
				++s1, --tail;
			else
				que[++tail] = s[i];
		printf("%d\n", s1 * 10 + (tail + 1 >> 1) * 5);
	}
	return 0;
}
