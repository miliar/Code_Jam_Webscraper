#include <iostream>
#include <stdio.h>
#include <string.h>
int panCakeFlip(char panCakeCol[]);

int main(int argc, char **argv)
{
	char panCol[101];
	int testCase;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&testCase);
	for(int i=0;i<testCase;i++){
		scanf("%s",panCol);
		int result = panCakeFlip(panCol);
		printf("Case #%d: %d\n", i+1,result);
	}
	return 0;
}
int panCakeFlip(char panCakeCol[]){

	int len = strlen(panCakeCol);
	int flip=0;
	for(int j=len-1;j>=0;j--)
	{	
		if(panCakeCol[j]=='-')
		{
			int k=j;
			int flag=0;
			for(k=j;k>=0;k--){
				if(panCakeCol[k]=='-'){
					flag=1;
					panCakeCol[k]='+';
				}else{
					flag=1;
					panCakeCol[k]='-';
				}
				
			}
		//	printf("### K: %d",k);
			if(flag==1)
				flip++;
		//	printf("### FLIP: %d",flip);
		}
	}
	return flip;

}	
	

