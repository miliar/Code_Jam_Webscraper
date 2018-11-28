#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int n,m,ans;
bool b[1002];
int num[1002];
void init()
{
	memset(b,0,sizeof(b));
	for(int i=1;i<=33;i++)
	{
		b[i*i]=1;
		num[i*i]=i;
	}
}

int main()
{	
	int t,i,j,co=0;
	scanf("%d",&t);
	char s[10];
	memset(num,0,sizeof(num));
	init();
	while(t--)
	{
		co++;ans=0;
		printf("Case #%d: ",co);
		scanf("%d%d",&i,&j);
		for(int k=i;k<=j;k++)
		{
			int flag=1;
			if(b[k]) {
				int left,right;
				sprintf(s,"%d",k);//cout<<s<<endl;
				int len=strlen(s);
			for(left=0,right=len-1;left<=right;left++,right--)
			    if(s[left]!=s[right]) {flag=0;break;}
			sprintf(s,"%d",num[k]);//cout<<s<<endl;
				len=strlen(s);
			for(left=0,right=len-1;left<=right;left++,right--)
			    if(s[left]!=s[right]) {flag=0;break;}	
			}
			if(b[k]&&flag) ans++;

		}
		printf("%d\n",ans);
	}
	return 0;
}

