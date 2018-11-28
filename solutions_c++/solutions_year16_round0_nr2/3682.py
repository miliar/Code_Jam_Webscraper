#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i,change,t,flag,len,p=0;
	char a[105];
	
		freopen("blarge.in","r",stdin);
		freopen("blarge1.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		p++;
	change=0;
	scanf(" %s",a);
	len=strlen(a);
//	printf("%sis str %c \n",a,a[len-1]);
	if(a[0]=='-')
	{
//		printf("inside -\n");
		flag=0;
		for(i=0;i<len;i++)
		{
			if(a[i]=='-'&&flag==1)
			{
				flag=0;
				change++;
			}
			if(a[i]=='+'&&flag==0)
			{
				flag=1;
				change++;
			}
			
		}
	}
	else if(a[0]=='+')
	{
		flag=1;
		//	printf("inside +\n");
		for(i=0;i<len;i++)
		{
			if(a[i]=='-'&&flag==1)
			{
				flag=0;
				change++;
			}
			if(a[i]=='+'&&flag==0)
			{
				flag=1;
				change++;
			}
			
		}
	}
//	printf("%c is a[len-1] %d \n",a[len-1],len-1);
	if(a[len-1]=='-')
	{
	//		printf("final inside -\n");
		change++;
	}
	printf("Case #%d: %d\n",p,change);
}
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
