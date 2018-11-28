
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long i8;
int k;
char str[1008];

int solve() {
	scanf("%s", str);
	scanf("%d", &k);
	int sz=strlen(str), re=0;
	for (int i=0; i+k<=sz; i++) 
		if (str[i]=='-') {
			re++;
			for (int j=0; j<k; j++)
				str[i+j]=(str[i+j]=='-'?'+':'-');
		}
	for (int i=sz-k; i<sz; i++)
		if (str[i]=='-')
			return -1;
	return re;
}

main() {
	int ccnt;
	scanf("%d", &ccnt);
	for (int cs=1; cs<=ccnt; cs++) {
		printf("Case #%d: ", cs);
		int re=solve();
		if (re<0) printf("IMPOSSIBLE\n");
		else printf("%d\n", re);
	}
}
