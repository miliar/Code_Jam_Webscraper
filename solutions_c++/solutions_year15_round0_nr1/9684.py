#include<stdio.h>

int main(){
	int t,i,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		int sm=0;
		scanf("%d",&sm);
		
		char a[sm+1];
		scanf("%s",a);

		
		int k,add,cnt=0,sum=a[0]-'0';
		for(k=1;k<sm+1;k++){
			add = a[k] - '0';
			if(sum<k){
				cnt++;
				sum=sum+add+1;
			}
			else
				sum+=add;
		}
	printf("Case #%d: %d\n",i,cnt);	
	}
return 0;
}

