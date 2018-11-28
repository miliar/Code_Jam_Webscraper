#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int test, cnt=1;
	scanf("%d",&test);
	while(test--) {
		char str[105];
		scanf("%s",str);
		printf("Case #%d: ", cnt++);
		int ans = 0;
		int leng = strlen(str);
		char last;
		for(int i=0;i<leng;i++) {
			if(i==0) {
				last = str[i];
			}
			if(last!=str[i]) {
				ans++;
				last = str[i];
			}
		}
		if(str[leng-1]=='-') {
			ans++;
		}
		printf("%d\n",ans);
	}
	
	return 0;
}
