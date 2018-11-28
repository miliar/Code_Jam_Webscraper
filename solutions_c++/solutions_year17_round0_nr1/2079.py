#include <cstdio>

char s[1005];
int k;

void sol() {
	scanf("%s%d", s, &k);
	int a = 0;
	for(int i = 0;s[i + k - 1];i++)
		if(s[i] == '-') {
			a++;
			for(int j = 0;j < k;j++) s[i + j] = s[i + j] == '+'? '-': '+';
		}
	for(int i = 0;s[i];i++) if(s[i] == '-') a = -1;
	if(a == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n", a);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1;i <= t;i++) printf("Case #%d: ", i), sol();
}
