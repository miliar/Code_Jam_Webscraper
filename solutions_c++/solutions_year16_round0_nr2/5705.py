#include<stdio.h>
#include<string.h>

int main()
{
	long long int t,c,i,k,ans,len;
	char s[150];

	FILE *fp=fopen("b.in","r");
	FILE *fp2 = fopen("bb2.out","w");

	fscanf(fp,"%lld ",&t);
	
	for(c=1;c<=t;c++)
	{
		ans=0;
		fscanf(fp,"%s",s);

		len=strlen(s);

		for(i=0;i<=len-2;i++)
		{
		if(s[i]!=s[i+1])
			{
				ans++;
			}
		}

		if(s[len-1]=='-')
		{
			ans++;
		}

		fprintf(fp2,"Case #%lld: %lld\n",c,ans);
	}
	return 0;
}
