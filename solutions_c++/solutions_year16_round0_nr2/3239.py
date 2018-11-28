#include<stdio.h>
#include<string.h>

char str[101];
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int T = 1; T <= tc; T++){
		scanf("%s", str);
		int ans = 0;
		int last = strlen(str) - 1;
		while (1){
			bool flag = false;
			int idx = -1;
			for (int i = last; i >= 0; i--){
				if (str[i] == '-'){
					idx = i;
					break;
				}
			}
			if (idx == -1){
				break;
			}
			for (int i = 0; i <= idx; i++){
				if (str[i] == '-'){
					str[i] = '+';
				}
				else{
					str[i] = '-';
				}
			}
			ans++;
		}
		printf("Case #%d: %d\n", T, ans);
	}
}