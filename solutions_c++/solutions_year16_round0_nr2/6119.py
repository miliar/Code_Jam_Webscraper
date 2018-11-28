#include<cstdio>
#include<cstring>

using namespace std;

int main() {
	int T; scanf("%d",&T);
	for(int cs=1;cs<=T;++cs) {
		printf("Case #%d:", cs);
		char s[105]; scanf("%s", s);
		int n = strlen(s);
		char bef = s[0];
		int ans = 0;
		for(int i=1;i<n;++i) {
			if(s[i] != bef) ans++;
			bef = s[i];
		}
		if(s[n-1] == '-') ans++;
		printf(" %d\n",ans);
	}
}
