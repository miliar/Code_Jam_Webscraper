#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	int t,n;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		char str1[105],str2[105];
		scanf("%s",str1);
		scanf("%s",str2);
		int p1=0,p2=0;
		int l1=strlen(str1);
		int l2=strlen(str2);
		int ans=0;
		int flag=1;
		while(p1<l1 && p2<l2)
		{
			if(str1[p1]!=str2[p2])
			{
				flag=0;
				break;
			}
			char ch=str1[p1];
			int temp1=0,temp2=0;
			while(str1[p1]==ch)
			{
				p1++;
				temp1++;
			}
			while(str2[p2]==ch)
			{
				p2++;
				temp2++;
			}
			temp1=temp1-temp2;
			if(temp1<0)
			temp1=temp1*(-1);
			ans=ans+temp1;
		}
		if(p1==l1 && p2<l2)
		{
			flag=0;
		}
		if(p1<l1 && p2==l2)
		{
			flag=0;
		}
		if(flag==0)
		{
			printf("Case #%d: Fegla Won\n",i);
		}
		else
		{
			printf("Case #%d: %d\n",i,ans);
		}
	}
	return 0;
}
