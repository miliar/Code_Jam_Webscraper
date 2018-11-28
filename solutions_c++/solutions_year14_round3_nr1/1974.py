#include<stdio.h>

int main(){
	int t,i,j,p,q,num_case=1;
	scanf("%d",&t);
	while(num_case<=t){
		int flag=1,gen=0;
		scanf("%d/%d",&p,&q);
		//printf("p=%d q=%d\n",p,q);
		while(q>p){
			if(q%2!=0){
				flag=0;
				break;
			}
			else{
				q=q/2;
				gen++;
			}
		//printf("p=%d q=%d gen=%d\n",p,q,gen);
		}
		while(q!=p){
			if(q%2!=0){
				flag=0;
				break;
			}
			else{
				q=q/2;
			}
		}
		if(flag || q==1)
			printf("Case #%d: %d\n",num_case++,gen);
		else
			printf("Case #%d: impossible\n",num_case++);
	}
	return 0;
}	
		
		