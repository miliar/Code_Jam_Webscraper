#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
char str[1005];
int main()
{
	int t,s,i,a=0,ans,j=1;
	freopen("A-large.in","r",stdin);
	freopen("out1.out","w",stdout);
	cin>>t;
	while(t--) {
		ans=0;
		a=0;
		scanf("%d",&s);
		scanf("%s",str);
		a=str[0]-'0';
		for(i=1;i<=s;i++) {
			if(str[i]!='0') {
				
			
			if(a<i) {
				ans=ans+(i-a);
				a=a+(i-a)+(str[i]-'0');
			}
			else {
				a=a+(str[i]-'0');
			}
		}
		}
		printf("Case #%d: %d\n",j++,ans);
	}
	return 0;
}
