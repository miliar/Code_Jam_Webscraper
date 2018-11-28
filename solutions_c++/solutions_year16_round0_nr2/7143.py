#include<stdio.h>
#include<string.h>
int main(){
	freopen("B-large.in","r",stdin);
    freopen("out.in","w",stdout);
     int t;
     scanf("%d",&t);
     int cnt=1;
     while(t--){
     	char s[105];
     	scanf("%s",&s);
     	int len=strlen(s);
     	int res=0;
     	for(int i=0;i<len;i++){
     		int flag=0;
     		while(s[i]=='-'){
     			i++;
     			flag=1;
			 }
			 if(flag==1){
			 	res++;
			 }
			while(s[i]=='+'){
				i++;
				flag=2;
			}
			if(flag==2&&i!=len){
				res++;
			}
			i--;
		 }
		 printf("Case #%d: ",cnt++);
		 printf("%d\n",res);
	 }
}
