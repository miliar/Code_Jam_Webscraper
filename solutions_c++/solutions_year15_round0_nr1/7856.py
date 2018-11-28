#include<stdio.h>
int n;
char a[1009];
int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int t;
	int tv=0;
	scanf("%d",&t);
	while(t--)
	{
		tv++;
		scanf("%d",&n);
		scanf("%s",a);
		int i, j, k;
		for(i=j=k=0;i<=n;i++)
		{
			if(j<i)
			{
				k+=i-j;
				j=i;
			}
			j+=a[i]-'0';
		}
		printf("Case #%d: %d\n",tv,k);
	}
}