#include<stdio.h>
#include<string.h>

int main()
{
	int tt,ca;
	char s[1000];
	int l,n,sum,num;
	int i,j,k;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&tt);
	for (ca=1;ca<=tt;ca++)
	{
		scanf("%s %d",s,&n);
		l=strlen(s);
		sum=0;
		for (i=0;i<=l-n;i++)
		{
			for (j=i+n-1;j<l;j++)
			{
				num=0;
				for (k=i;k<=j;k++)
				{
					if (s[k]=='a'||s[k]=='e'||s[k]=='i'||s[k]=='o'||s[k]=='u') num=0; 
						else num++;
					if (num>=n) break;
//					printf("%c",s[k]);
				}
//				printf("\n",i,j);
				if (num>=n) sum++;
			}
		}
		printf("Case #%d: %d\n",ca,sum);
	}
	return 0;
}
			