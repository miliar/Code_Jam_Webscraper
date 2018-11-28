#include<stdio.h>
#include<string.h>
#define size 105
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int ans[size];
	for(int k=0;k<t;k++)
	{
		char str[size];
		char symbol='-';
		int flag=1,cnt=0;
		scanf("%s",str);
		int len=strlen(str);
		for(int i=len-1;i>=0;i--)
		{
			if(flag==1 && str[i]=='+')
				continue;
			else if(flag==1 && str[i]=='-')
			{
				cnt++;
				flag=0;
				while(str[i-1]=='-')
					i--;
				symbol='+';
			}
			else if(flag==0 && str[i]==symbol)
			{
				cnt++;
				while(str[i-1]==symbol)
					i--;
				if(symbol=='-')
					symbol='+';
				else symbol='-';
			}
		}
		ans[k]=cnt;
	}
	for(int k=0;k<t;k++)
		printf("Case #%d: %d\n",k+1,ans[k]);			
	return 0;
}
