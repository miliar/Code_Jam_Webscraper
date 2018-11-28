#include<stdio.h>
#include<string>
using namespace std;
char s[22222];
char st[22222];
int top;
int main(){
	int _;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		scanf("%s",s);
		top=0;
		int res=0;
		for(int i=0; s[i]; i++)
			if(top>0 && s[i] == st[top-1]){
				res+=10;
				top--;
			}else
				st[top++]=s[i];
		printf("Case #%d: %d\n",T,res+top/2*5);
	}
	return 0;
}