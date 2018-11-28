#include <stdio.h>
#include <string.h>

int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t); getchar();
	for(int i=1;i<=t;i++){
		char str[1010]={0},ans[3000]={0};
		int left=999,right=1001;
		scanf("%s",str);
		ans[1000]=str[0];
		int len=strlen(str);
		for(int j=1;j<len;j++){
			if(str[j]>=ans[left+1]){
				ans[left]=str[j];
				left-=1;
			}
			else{
				ans[right]=str[j];
				right+=1;
			}
		}
		printf("Case #%d: ",i);
		left=left+1;
		for(left;left<right;left++) printf("%c",ans[left]);
		printf("\n");
	}
	
	return 0;
}
