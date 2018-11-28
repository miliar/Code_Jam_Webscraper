#include<stdio.h>

int main(){
	int t,j;
	scanf("%d", &t);
	for(j=1;j<=t;j++){
		int s;
		scanf("%d", &s);
		char string[1002];
		scanf("%s", string);
		int i, m=0, n=0;
		for(i=0;i<=s;i++){
			int members = string[i] - '0';
			if(m >= i){
				m +=  members;
			}
			else{
				n += i - m;
				m = i + members;
			}
		}
		printf("Case #%d: %d\n",j, n);
	}
	return 0;
}
