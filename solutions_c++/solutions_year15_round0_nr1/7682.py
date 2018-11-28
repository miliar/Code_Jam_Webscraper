#include<stdio.h>
void DO(){
	int n,i,count=0,need=0;
	char s[1010];
	scanf("%d%s",&n,s);
	for(i=0;i<=n;i++){
		if(count<i&&s[i]!='0'){
			need += i - count;
			count = i;
		}
		count+=s[i]-'0';
	}
	printf("%d\n",need);
}
int main(){
	int T,t;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		DO();	
	}
}
