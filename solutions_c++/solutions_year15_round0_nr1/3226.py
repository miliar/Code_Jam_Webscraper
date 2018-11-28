#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int n;
char s[1005];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d",&n);
		scanf("%s",s);
		int tot = 0,ret = 0;
		for (int i=0; i<=n; i++) {
			if (tot >= i) tot += s[i]-'0';
			else if (s[i] > '0') {
				ret += i-tot;
				tot += i-tot+s[i]-'0';
			}
		}
		printf("Case #%d: %d\n",t,ret);
	}
    return 0;
}
