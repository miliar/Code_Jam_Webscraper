#include<stdio.h>
#include<string.h>
main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("output_file.out","w",stdout);
	int t,ans,ca=0,l,i;
	char s[101];
	scanf("%lld",&t);
	while(t--)
	{
		ans=0;
		ca++;
		scanf("%s",&s);
		l=strlen(s);
		if(s[l-1]=='-')
		{
			ans++;
		}
		for(i=0;i<l-1;i++)
		{
			if(s[i]!=s[i+1])
			{
				ans++;
			}
		}
		printf("Case #%d: %lld\n",ca,ans);
	}
	return 0;
}
