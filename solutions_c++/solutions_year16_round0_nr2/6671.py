#include <stdio.h>
#include <string.h>

char cookie[105];
void reverse(int bound){
	char tmp[105];
	for(int i=0;i<=bound;i++){
		tmp[i] = cookie[i];
	}
	for(int i=0, j=bound;i<=bound;i++, j--){
		if(tmp[j]=='-')
			cookie[i] = '+';
		else
			cookie[i] = '-';
	}

}
int main(){

	int tn, t, ans, len, inx;
	scanf("%d\n", &tn);
	for(int t=1;t<=tn;t++){

		scanf("%s", cookie);
		len = strlen(cookie);
		char now;
		ans = 0;
		now = cookie[0];
		for(int i=1;i<len;i++){
			if(now != cookie[i]){
				ans++;
				now = cookie[i];
			}
		}
		if(cookie[len-1]=='-')
			ans++;
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}