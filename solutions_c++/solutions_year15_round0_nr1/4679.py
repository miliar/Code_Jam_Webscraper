#include<bits/stdc++.h>
using namespace std;


int main(){
	int tc, smax, tot, ans, n;
	char str[1005];

	scanf("%d", &tc);
	for (int cc = 1; cc <= tc; cc++){
		tot = ans = 0;
		scanf("%d %s", &n, &str);
		int len = strlen(str);
		for (int i = 0; i < len; i++){
			if (tot >= len) break;

			int num = (int)str[i] - '0';
			
			if (num == 0) continue;
			
			if (tot < i){
				int diff = i - tot;
				tot += diff;
				ans += diff;
			}
			tot += num;
			// printf("tot %d ans %d\n", tot, ans);
		}
		printf("Case #%d: %d\n", cc, ans);
	}

	return 0;
}