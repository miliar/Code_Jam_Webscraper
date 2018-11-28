#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
char arr[100][100];
int l[100];
int main()
{
	int n,t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			scanf("%s",arr[j]);
			l[j]=strlen(arr[j]);
		}
		int k=0,ll=0,count=0,f=1,c0,c1;
		char ch0,ch1;
		while(k<l[0]  &&  ll<l[1])
		{
		c0=1;
		c1=1;
		ch0=arr[0][k];
		ch1=arr[1][ll];
		if(ch0 != ch1)
		f=0;
			while(arr[0][k]==ch0  && k<l[0]  )
			{
			k++;
			c0++;
			}
			while(arr[1][ll]==ch1  && ll<l[1]  )
			{
			ll++;
			c1++;
			}
			if(c1>c0)
			count+=(c1-c0);
			else
			count+=(c0-c1);
		}
		if(k<l[0] || ll<l[1])
		f=0;
		printf("Case #%d: ",i);
		if(f==1)
		printf("%d\n",count);
		else
		printf("Fegla Won\n");
	}
return 0;
}
