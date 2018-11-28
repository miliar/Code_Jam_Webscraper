#include<stdio.h>
#include<string.h>

int main(){
	int t,c=1,i,j,l,len,max;
	char s[1005];
	scanf("%d",&t);
	while(t--){
		char ans[1005];
		scanf("%s",s);
		l=strlen(s);
		max=s[0];
		ans[0]=s[0];
		ans[1]='\0';
		for(i=1;i<l;i++){
			len=strlen(ans);
			if(s[i]>=max){
				max=s[i];
				for(j=len;j>0;j--)
					ans[j]=ans[j-1];
				ans[len+1]='\0';
				ans[0]=s[i];
				//printf("%c %s\n",s[i],ans);
			}else{
				ans[len]=s[i];
				ans[len+1]='\0';
			}
		}
		
		printf("Case #%d: %s\n",c++,ans);
	}
	
	return 0;
}
