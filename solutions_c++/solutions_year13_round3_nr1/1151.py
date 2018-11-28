#include <cstdio>

char s[1000001];
int v[1000001];
int main() {
	int tc, n;
	int map[256]={0};
	const char *ms = "aiueo";
	for(int i='a'; i<='z'; i++)
		map[i] = 1;
	for(int i=0; ms[i]; i++)
		map[ms[i]] = 0;
	scanf("%d", &tc);
	for(int cs=1; cs<=tc; cs++) {
		printf("Case #%d: ", cs);
		scanf("%s %d", s, &n);
		int l = 0;
		for(int i=0; s[i]; i++, l++)
			v[i] = map[s[i]] ? 1 + (i>0?v[i-1]:0) : 0;
		//for(int i=0; i<l ; i++)
			//printf("%d ", v[i]); puts("");
		int result = 0;
		for(int i=0, p = l - n; i <= p; i++) {
			for(int j = i + n - 1; j < l; j++)
				if(v[j] >= n) {
					result += l-j;
					break;
				}
		}
		printf("%d\n", result);
	}
	return 0;
}
