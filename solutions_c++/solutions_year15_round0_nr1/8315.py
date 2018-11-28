#include<stdio.h>
int t,n,i,j;
long long int sum,ans;
char s[1001];
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		scanf("%d",&n);
		getchar();
		scanf("%s",s);
		sum=(s[0]-'0');
		ans=0;
		for(j=1;s[j]!='\0';++j)
		{
			if((s[j]-'0')!=0 && sum < j)
			{
				ans += (j-sum);
				sum += (j-sum);
			}
			sum += (s[j]-'0');
		}
		printf("Case #%d: %d\n",i,ans);
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
