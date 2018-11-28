#include<stdio.h>
#include<string>
using namespace std;
char s[9999];
int main(){
	int _,m,n;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		scanf("%d%d",&m,&n);
		bool nosol=false;
		for(int i=0; i<m; i++){
			scanf("%s",s);
			bool flag=true;
			for(int j=0; j<n; j++)
				if(s[j]=='0')
					flag=false;
			if(flag)
				nosol=true;
		}
		scanf("%*s");
		printf("Case #%d: ",T);
		if(nosol){
			puts("IMPOSSIBLE");
			continue;
		}
		if(n==1){
			printf("0 ?\n");
			continue;
		}
		for(int i=0; i<36; i++)
			printf("10");
		printf("10?");
		for(int i=0; i<36; i++)
			printf("10");
		printf("1");
		printf(" ");
		for(int i=1; i<n; i++)
			printf("?");
		puts("");
	}
	return 0;
}
