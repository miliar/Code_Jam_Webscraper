#include<stdio.h>
#include<string.h>
int main(){
	int t,j=1,l,count,i;
	char stack[100],last;
	scanf("%d",&t);
	while(t--){
		scanf("%s",stack);
		l=strlen(stack);
		count=0;
		last=stack[0];
		for(i=1;i<l;i++){
			if(stack[i]!=last){
				count++;
				last=stack[i];
			}
		}
		if(last=='-')
			count++;
		printf("Case #%d: %d\n",j++,count);
	}
	return 0;
}
