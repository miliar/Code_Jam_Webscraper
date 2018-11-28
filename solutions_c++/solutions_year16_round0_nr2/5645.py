#include<stdio.h>
int main(){
	long long int test,i,j,k,n;
	scanf("%lld",&test);
	for(i=1;i<=test;i++){
		char arr[300];
		scanf("%s",&arr);
		k=0;
		if(arr[0]=='-'){
			k=1;
		}
		for(j=1;arr[j]!='\0';j++){
			if((arr[j]=='-') && (arr[j-1]=='+'))
			{
				k=k+2;
			}
		}
		printf("Case #%lld: %lld",i,k);
		printf("\n");
	}
	return 0;
}
