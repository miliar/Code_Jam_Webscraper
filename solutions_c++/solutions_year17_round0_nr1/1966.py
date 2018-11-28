#include<bits/stdc++.h>
using namespace std;
char str[1010];
int main(){
	int K,tcase,kase=0;
	scanf("%d",&tcase);
	while(tcase--){
		scanf("%s%d",str,&K);
		int len=strlen(str),ans=0;
		for(int i=0;i<=len-K;i++){
			if(str[i]=='-'){
				for(int j=i;j<i+K;j++){
					if(str[j]=='-') str[j]='+';
					else if(str[j]=='+') str[j]='-';
				}
				ans++;
			}
		}
		bool ok=true;
		for(int i=len-K;i<len && ok;i++)
			if(str[i]=='-') ok=false;
		printf("Case #%d: ",++kase);
		if(ok) printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}
