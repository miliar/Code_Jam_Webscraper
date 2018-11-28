#include <stdio.h>

int t,n;
char s[1010];

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;++tt){
		scanf("%d %s",&n,s);
		int res=0,total=0;
		for(int i=0;i<=n;++i){
			if (s[i]>'0'){
				if (i>total){
					res+=i-total;
					total=i;
				}
				total+=s[i]-'0';
			}
		}
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;
}
