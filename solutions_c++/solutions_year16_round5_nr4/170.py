#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	scanf("%d",&T);
	char s[200];
	for(int cs=1;cs<=T;cs++){
		int n,l;
		scanf("%d%d",&n,&l);
		bool gg=false;
		for(int i=0;i<n;i++){
			scanf("%s",s);
			int c0=0;
			for(int j=0;j<l;j++){
				c0+=s[j]=='0';
			}
			if(!c0) gg=true;
		}
		scanf("%s",s);
		printf("Case #%d:",cs);
		if(gg) puts(" IMPOSSIBLE");
		else if(l==1) puts(" 0 ?");
		else{
			printf(" 10?");
			for(int i=1;i<l;i++) putchar('0'+(i&1));
			printf(" ");
			for(int i=1;i<l;i++) printf("?");
			puts("");
		}
	}
	return 0;
}