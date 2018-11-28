#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int N=2000;
char s[N];

char sw(char c) {
	if(c=='+') return '-';
	return '+';
}

int main() {
	int ncase, icase, i, j, k, n, ans;
	scanf("%d", &ncase);
	for(icase=1; icase<=ncase; icase++) {
		scanf("%s%d", s, &k);
		ans=0;
		n=strlen(s);
		for(i=0; i+k<=n; i++) if(s[i]=='-') {
			ans++;
			for(j=i; j<i+k; j++) s[j]=sw(s[j]);
		}
		for(; i<n; i++) if(s[i]=='-') break;
		if(i<n) printf("Case #%d: IMPOSSIBLE\n", icase);
		else printf("Case #%d: %d\n", icase, ans);
	}
	return 0;
}