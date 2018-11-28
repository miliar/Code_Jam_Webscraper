#include <stdio.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int i=0; i<T; i++){
		int Smax;
		scanf("%d",&Smax);
		char a[Smax+1];
		for(int j=0; j<=Smax; j++){
			scanf(" %c",a+j);
			a[j] = a[j]-'0';
		}
		int cnt = 0, ans = 0;
		for(int j=0; j<=Smax; j++){
			if(cnt < j){
				ans += j-cnt;
				cnt = j;
			}
			cnt += a[j];
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
