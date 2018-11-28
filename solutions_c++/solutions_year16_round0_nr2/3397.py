#include <bits/stdc++.h>
void switchArr(char s[],int len,int lim)
{
	char a[111];
	int i;
	for(i=lim;i>=0;i--)
	{
		a[lim-i]=s[i]=='+'?'-':'+';
	}
	for(i=0;i<=lim;i++)
		s[i]=a[i];
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	long long t,i,T,len,count,lim;
	char s[111];
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		getchar();
		scanf("%s",s);
		len=strlen(s);
		count=0;
		while(1)
		{
			for(i=len-1;i>=0&&s[i]=='+';i--);
			if(i==-1)
				break;
			lim=i;
			for(i=0;i<=lim&&s[i]=='+';i++);
			if(i!=0)
			{
				switchArr(s,len,i-1);
				switchArr(s,len,lim);
				count+=2;
			}
			else
			{
				switchArr(s,len,lim);
				count++;	
			}
		}
		printf("Case #%lld: %lld\n",t,count);
	}
	return 0;
}