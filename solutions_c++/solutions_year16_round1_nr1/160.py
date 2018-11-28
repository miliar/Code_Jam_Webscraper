#include <cstdio>
#include <cstring>

const int MAXN = 1E3 + 10;

char s[MAXN], s0[MAXN << 1];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%s", s);
		int n = strlen(s);
		int l = n, r = n, pre = 0;
		for (int i = 0; i < n; ++i){
			if (pre <= s[i])
				s0[--l] = pre = s[i];
			else
				s0[r++] = s[i];
		}
		s0[r] = '\0';
		puts(s0 + l);
	}
	return 0;
}
