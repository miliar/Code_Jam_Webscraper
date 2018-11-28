#include<stdio.h>
#include<string>
#include<math.h>
using namespace std;

int fun(__int64 x)
{
	char qq[100],ww[100];
	sprintf(qq,"%I64d",x);
	int len=strlen(qq);
	for(int i=0;i<len;i++)
		ww[i]=qq[len-i-1];
	ww[len]='\0';
	char qqq[202],www[202];
	strcpy(qqq,qq);
	strcpy(www,ww);
	
	strcat(qqq,ww);
	strcat(www,qq);
	//printf("%s %s\n",qqq,www);
	if(strcmp(qqq,www)==0)
		return 1;
	else
		return 0;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin) ;
	freopen("C-small-attempt0.out","w",stdout) ;
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int s=0;
		__int64 a,b;
		scanf("%I64d%I64d",&a,&b);
		for(__int64 i=a;i<=b;i++)
		{
			__int64 xx=(__int64)sqrt(i);
			if(xx*xx==i&&fun(xx)&&fun(i))
			{
				//printf("%I64d\n",i);
				s++;
			}
		}
		printf("Case #%d: %d\n",k,s);
	}
	return 0;
}
