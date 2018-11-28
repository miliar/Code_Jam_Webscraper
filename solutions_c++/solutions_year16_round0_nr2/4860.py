#include<stdio.h>
#include<string.h>

char s[105];

int main(){
	freopen("out.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int q=1;q<=T;++q){
		scanf("%s",s);
		int l=strlen(s);
		for(int i=l-1;i>=0;--i){
			if(s[i]=='+')s[i]=0;
			else break;	
		}
		l=strlen(s);
		printf("Case #%d: ",q);
		if(l){
			int ans=1;
			for(int i=1;i<l;++i){
				if(s[i]!=s[i-1])ans++;	
			}
			printf("%d\n",ans);
		}
		else printf("0\n");
	}
	return 0;
}
