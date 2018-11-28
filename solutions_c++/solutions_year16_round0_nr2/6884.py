#include<stdio.h>
#include<string.h>
int main(){
	freopen("B-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	int num, T;
	char s[101][101];
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%s",&s[i]);
		num = 0;
		for(int j=strlen(s[i])-1;j>=0;j--){
			if(s[i][j]=='-'){
				for(int k=j;k>=0;k--){
					s[i][k] = '+'+'-'-s[i][k];
				}
				num++;
			}
		}
		printf("Case #%d: %d\n",i+1,num);	
	}
}
