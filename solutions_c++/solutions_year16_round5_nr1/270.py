#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char s[25000],hv[25000];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%s",s);
		int n = strlen(s);
		int at = 0,mat = 0;
		for (int i=0; i<n; i++) {
			if (at && hv[at-1] == s[i]) {
				at--;
				mat++;
				continue;
			}
			hv[at++] = s[i];
		}
		printf("Case #%d: %d\n",t,n/2*5+mat*5);
	}
    return 0;
}
