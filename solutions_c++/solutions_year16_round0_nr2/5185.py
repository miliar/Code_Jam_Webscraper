#include <stdio.h>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
char str[200];
int main(void)
{
	int t,cas=0;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%s",str);
		int len=strlen(str);
		int ans=0;
		int flag=0;
		for(int i=0;i<len;i++){
			if(i==0){
				if(str[i]=='+')flag=1;
				else flag=0;
				continue;
			}
			if(i==len-1){
				if(str[i]=='+'){
					if(flag==0)ans++;
					flag=1;
				}
				else {
					ans++;
					if(flag==1)ans++;
					flag=1;
				}
				continue;
			}
			if(str[i]=='+'){
				if(flag==0)ans++;
				flag=1;
			}
			else{
				if(flag==1)ans++;
				flag=0;
			}
		}
		if(!flag)ans++;
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
