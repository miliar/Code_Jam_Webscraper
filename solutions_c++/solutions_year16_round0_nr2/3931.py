#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<bitset>
#include<cstring>

using namespace std;


int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,x;
	char s[105];
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		scanf("%s",s);
		int len = strlen(s);
		s[len] = '+';
		int ans=0;
		for(int i=1;i<=len;i++)
			if(s[i]!=s[i-1])
				ans++;
		printf("Case #%d: %d\n",cas,ans);
	}
	
	
	return 0;
} 
