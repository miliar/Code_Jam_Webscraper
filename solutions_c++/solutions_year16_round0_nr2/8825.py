#include<stdio.h>
int main(){
	int t , i , j , count , flag;
	char str[101] , ch;
	
	scanf("%d",&t);
	
	i=1;
	while(i<=t){
		
		scanf("%s",str);
		count=0;
		
		ch=(str[0]=='+')?'+':'-';
		
		for(j=1; str[j]!='\0';j++){
		    
			if(str[j]!=ch){
				ch = str[j];
				count++;
				//printf("%c  %d\n",ch,count);
			}
		}
		
		if(ch=='-')
		  count++;
		printf("CASE #%d: %d\n",i,count);
		i++;
	}
	return 0;
}
