#include<cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int nm=1;nm<=T;nm++) {
		int n;
		scanf("%d", &n);
		n++;
		char cnum[1001];
		scanf("%s", cnum);
		int num[1000];
		for (int i=0;i<n;i++) {
			num[i] = cnum[i] - '0';
		}
		int ct= 0, ans= 0;
		for (int i=0;i<n;i++) {
			if (i > ct) {
				ans+= i - ct;
				ct+= i - ct;
			}
			ct+= num[i];
		}
		printf("Case #%d: %d\n", nm, ans);
	}
	return 0;
}
