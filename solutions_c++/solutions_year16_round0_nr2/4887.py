#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>

using namespace std;
char s[120];
int a[120],b[120];

int main()
{
	int t,n;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int ca=0;
	while(t--)
	{
		ca++;
		scanf("%s",s);
		printf("Case #%d: ",ca);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		int len=strlen(s);
		for(int i=0;i<len;i++)
			if(s[i]=='-')
				a[i+1]=0;
			else
				a[i+1]=1;
		int count=0;
		for(int i=len;i>=1;i--)
		{
			if(a[i]==0&&b[i]%2==0||a[i]==1&&b[i]%2==1)
			{
				b[i-1]=b[i]+1;
				count++;
			}
			else
				b[i-1]=b[i];
		}
		printf("%d\n",count);
	}
 	return 0;
}


