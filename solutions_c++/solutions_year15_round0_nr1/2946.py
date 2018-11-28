#include<stdio.h>
#include<string.h>

char s[2000];

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		int n;
		scanf("%d",&n);
		scanf("%s",s);
		int ans = 0;
		int sum = 0;
		for(int i = 0;i <= n;++i){
			int now = s[i] - '0';
			if(sum + ans < i){
				ans = i - sum;
			}
			sum += now;
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

