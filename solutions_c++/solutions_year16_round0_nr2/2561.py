#include<stdio.h>
#include<string.h>
int tc,tcn;
int n;
char s[110];
int ans;
int main(){
	int i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%s",s);
		n=strlen(s);
		s[n]='+';
		ans=0;
		for(i=0;i<n;i++){
			if(s[i]!=s[i+1])ans++;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}