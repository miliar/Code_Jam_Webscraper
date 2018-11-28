#include<bits/stdc++.h>
using namespace std;
char s[110];
void fuck()
{
	int i,j,l,ans=0;
	scanf("%s",s+1);
	l=strlen(s+1);
	for(i=l;i>=1;i--){
		if(s[i]=='-'){
			++ans;
			for(j=1;j<=i;j++)
				s[j]=s[j]=='+'?'-':'+';
		}
	}
	printf("%d\n",ans);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		fuck();
	}
 return 0;
}

