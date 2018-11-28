#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)

int tc;
int k;
char a[1234];
int main() {
	scanf("%d", &tc);
	fo(_,1,tc+1) {
		printf("Case #%d: ", _);
		scanf("%s %d", a, &k);
		int n = strlen(a);
		int ans = 0;
		fo(i,0,n-k+1) if (a[i]=='-') {
			ans++;
			fo(j,0,k) {
				if (a[i+j]=='+') a[i+j] = '-';
				else a[i+j]='+';
			}

		}
		char g = 1;
		fo(i,0,n) if (a[i]=='-') g = 0;
		if (!g) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}

	return 0;
}