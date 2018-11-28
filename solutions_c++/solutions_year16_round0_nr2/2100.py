#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,ans,i;
	char stack[200];
	scanf("%d",&t);

	for(int cas=1;cas<=t;cas++){
		ans=0;
		scanf("%s",stack);
		for(i=0;stack[i]!='\0';i++){
			if(stack[i]=='-'){
				ans=ans+2;
				while(stack[i]=='-'&&stack[i]!='\0'){
					i++;
				}
				i--;
			}
		}
		if(stack[0]=='-')
			ans--;
		printf("Case #%d: %d\n",cas, ans);
	}
	return 0;
}