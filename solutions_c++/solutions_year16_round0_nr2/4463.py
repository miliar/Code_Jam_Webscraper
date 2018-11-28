#include <iostream>
#include <cstdio>
using namespace std;
int had[10];
char s[105];
int main(){
	int T,cases,n,ans;
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){
		printf("Case #%d: ",cases);  
		scanf("%s",s+1),n=strlen(s+1);
		ans=0;
		if (s[1]=='-') ans=1;
		for (int i=2;i<=n;i++){
			if (s[i]==s[i-1]) continue;
			if (s[i]=='+') continue;
			ans+=2;
		}
		printf("%d\n",ans);
	}
	return 0;
}