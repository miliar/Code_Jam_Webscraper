#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

char s[2000];
int a[2000];


int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, k;
	scanf("%d", &T);
	for (int tt = 1; tt <= T;tt++){
		printf("Case #%d: ", tt);
		scanf("%s%d", s, &k);
		int n = strlen(s);
		for (int i = 0;i < n;i++){
			if (s[i] == '+') a[i] = 1;
			else a[i] = 0;
		}
		int ans = 0;
		for (int i = 0;i < n;i++){
			if (a[i] == 0){
				if (i + k > n){
					ans = -1;
					break;
				}
				ans++;
				for (int j = i;j < i + k;j++){
					a[j] = a[j] ^ 1;
				}
			}
		}
		if (ans == -1){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n", ans);
		}
	}
	return 0;
}
