#include<stdio.h>
char s[10000];
int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0 ; e < t ; e++ ){
		int len ;
		int ans = 0;
		scanf("%d",&len);
		scanf("%s",s);
		int num = 0;
		for(int i = 0 ; i < len+1 ; i++){
			int ct = s[i]-'0';
			if( num < i && ct > 0 ){
				ans += i-num;
				num += i-num;
			}
			num += ct;
		}
		printf("Case #%d: %d\n",e+1,ans);
	}
}

