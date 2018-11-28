#include <bits/stdc++.h>
using namespace std;

int t, smax, stand, len, ans;
char st[1005];

int main(){
	scanf("%d", &t);
	for(int tc = 1 ; tc <= t ; tc++){
		scanf("%d", &smax);
		getchar();
		scanf("%s", st);
		stand = 0;
		len = strlen(st);
		ans = 0;
		stand += st[0] - '0';
		for(int i = 1 ; i < len ; i++){
			if(stand < (i)){
				ans += (i) - stand;
				stand += (i) - stand;
			}
			stand += st[i] - '0';
		}
		printf("Case #%d: %d\n", tc, ans);
	}
}
