#include <stdio.h>
#include <string.h>

__int64 a[100];

int hui(__int64 i)
{
	char b[100];
	sprintf(b,"%I64d",i);
	int len=strlen(b);
	//printf("%d\n",len);
	for(int i=0;i<len/2;i++)
		if(b[i]!=b[len-i-1])
			return 0;
	return 1;
}

int main(int argc, char const *argv[])
{
	freopen("C-large-1.in","r",stdin);
	freopen("Big1Coutput.txt","w",stdout);
	int num=0;
	for(__int64 i=1;i<=10000000;i++)
	{
		__int64 j=i*i;
		//printf("%d %d\n",i,j);
		if(hui(i) && hui(j))
		{
			a[num++]=j;
		}
	}
	//printf("num!:%d\n",num);
	//for(int i=0;i<num;i++)
		//printf("%I64d\n",a[i]);
	int t,cass=1;
	__int64 s,e;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%I64d %I64d",&s,&e);
		int m=0;
		for(int i=0;i<num;i++)
			if(a[i]>=s&&a[i]<=e)
				m++;
		printf("Case #%d: %d\n",cass++,m);
	}
	return 0;
}
