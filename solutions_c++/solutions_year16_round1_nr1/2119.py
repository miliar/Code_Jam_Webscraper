#include <stdio.h>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<iostream>
using namespace std;
char str[1040];
int ss[1040];
char ans[1040];
int main(void)
{
	int t,cas=0;
freopen("A-large.in","r",stdin);
freopen("large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%s",str+1);
		int len=strlen(str+1);
		int flag=0;
		char mx=0;
		memset(ss,0,sizeof(ss));
		memset(ans,0,sizeof(ans));
		for(int i=1;i<=len;i++){
			if(str[i]>=mx){
				mx=str[i];
				ss[i]=i;
			}
		}
		int st=1,ed=len;
		for(int i=len;i>=1;i--){
			if(ss[i]==i)
			ans[st++]=str[i];
			else ans[ed--]=str[i];
		}
		printf("Case #%d: %s\n",++cas,ans+1);
	}
	return 0;
}
