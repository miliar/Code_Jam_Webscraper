#include <cstdio>
#include <cstdlib>
#include <cstring>

int t,n,i,ans,tes,stand;
char s[10007];

int main() {
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d%s",&n,&s);
		
		ans = 0;
		stand = 0;
		
		for (i=0 ; i<=n ; i++) {
			while (s[i] - '0' > 0 && stand < i) {
				ans++;
				stand++;
			}
			
			stand += s[i] - '0';
		}
		
		printf("Case #%d: %d\n",tes,ans);
	}
}
