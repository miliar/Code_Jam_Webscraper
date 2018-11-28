#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char str[105];
int ok[105];

int main(){
	int T, kase = 0;
	freopen("Bin2.txt", "r", stdin);
	freopen("Bout2.txt", "a", stdout);
	scanf("%d", &T);
	while(T--){
		scanf("%s", str);
		int n = strlen(str), flip = 0;
		for(int i = 0; i < n; i++){
			if(str[i] == '-'){
				ok[i] = 0;
			}
			else{
				ok[i] = 1;
			}
		}
		int cnt = 0;
		for(int i = n-1; i >= 0; i--){
			if(ok[i]^flip == 0){
				flip ^= 1;
				cnt++;
			}
		}
		printf("Case #%d: ", ++kase);
		printf("%d\n", cnt);
	}
}
