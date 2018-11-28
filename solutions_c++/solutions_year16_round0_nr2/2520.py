#include <cstdio>
#include <cstring>
int main (){
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);
	int T;
	char s[101];
	scanf("%d\n", &T);
	for (int i = 1; i <= T; i++){
		gets(s);
		int len = strlen(s);
		int cnt = 0;
		for (int j = 1; j < len; j++)
			if (s[j - 1] != s[j])
				cnt++;
		if (s[len - 1] == '-')
			cnt++;
		printf("Case #%d: %d\n", i, cnt);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
