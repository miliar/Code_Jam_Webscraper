#include <stdio.h>
#include <string.h>

struct ss
{
	char a;
	int num;
}str[105][105];
int count,sum[105],ans;

double half;
int T,n,i,j,k;
int main()
{
	char s[105];
	int len,index;
	bool check;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	scanf("%d",&T);
	for(i=1; i<=T; i++)
	{
		scanf("%d",&n);
		check = true;
		ans = 0;
		for(j=0; j<n;j++)
		{
			scanf("%s",s);
			str[j][0].a = s[0];
			str[j][0].num++;
			k=0;
			index=1;
			len = strlen(s);
			while(index<len)
			{
				if(s[index] == s[index-1])
					str[j][k].num++;
				else
				{
					k++;
					str[j][k].a = s[index];
					str[j][k].num++;
				}
				index++;
			}
			if(j==0)
				count = k+1;
			if(j>0 && count!=k+1)
				check = false;
			
		}
		for(j=1; j<n; j++)
		{
			for(k=0; k<count; k++)
			
				if(str[j-1][k].a != str[j][k].a)	
					check = false;
		}
		if(check)
		{
			for(k=0; k<count; k++)
			{
				sum[k] = 0;
					for(j=0; j<n;j++)
					sum[k] += str[j][k].num;
			}
			half = n;
				half/=2;
			for(k=0; k<count; k++)
			{
	
				if(sum[k]%n<half)
					sum[k]/=n;	
				else
					sum[k] = sum[k]/n+1;
			}
			for(j=0; j<n; j++)
			{
				for(k=0; k<count; k++)
				{
					if(str[j][k].num > sum[k])
						ans += str[j][k].num - sum[k];
					else
						ans += sum[k]-str[j][k].num;
				}
			}
			/*
			for(k=0; k<count; k++)
			{
				if(str[0][k].num < str[1][k].num)
					ans += str[1][k].num-str[0][k].num;
				else
					ans += str[0][k].num-str[1][k].num;
			}
			*/
			printf("Case #%d: %d\n",i,ans);
		}
		else
			printf("Case #%d: Fegla Won\n",i);

		for(j=0; j<n; j++)
			for(k=0; k<100; k++)
				str[j][k].num = 0;
	}
}

