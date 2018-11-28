#include <stdio.h>
#include <string.h>

char g[110][60];
char b[60];
char anss1[210] ,anss2[210];
char as[60];
char bs[60];
int a[60];
int main(void)
{
	int tt ,ii;
	int n ,l ,i ,j ,jj;
	int ans;
	int m;
	int cc;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&n ,&l);
		for (i=1 ; i<=n ; i++)
		{
			scanf("%s" ,g[i]);
		}
		scanf("%s" ,b);
		ans=1;
		for (i=1 ; i<=n ; i++)
		{
			if (strcmp(g[i],b)==0)	
			{
				ans=0;
				break;	
			}
		}
		printf("Case #%d: " ,ii);
		if (ans)
		{
			for (i=0 ; i<l ; i++)
			{
				if (b[i]=='1')
				{
					anss2[i*2]='0';	
				}
				else
				{
					anss2[i*2]='1';						
				}
				anss2[i*2+1]='?';					
			}			
			anss2[l*2]=0;
			m=1;
			as[m]=b[0];
			if (as[m]=='1')
			{
				bs[m]='0';	
			}
			else
			{
				bs[m]='1';					
			}
			a[m]=1;
			for (i=1 ; i<l ; i++)
			{
				if (b[i]==b[i-1])
				{
					a[m]++;
				}
				else
				{
					m++;
					as[m]=b[i];
					if (as[m]=='1')
					{
						bs[m]='0';	
					}
					else
					{
						bs[m]='1';					
					}					
					a[m]=1;
				}
			}
			cc=0;
			for (i=1 ; i<m ; i++)
			{
				jj=a[i];
				for (j=1 ; j<jj ; j++)
				{
					anss1[cc]=as[i];
					cc++;					
				}
				anss1[cc]=bs[i];
				cc++;													
				anss1[cc]=as[i];
				cc++;									
			}
			jj=a[m];
			for (j=1 ; j<jj ; j++)
			{
				anss1[cc]=as[m];
				cc++;					
			}
			anss1[cc]=bs[m];
			cc++;					
			anss1[cc]=0;
			printf("%s %s\n" ,anss1 ,anss2);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	
	return 0;
}
