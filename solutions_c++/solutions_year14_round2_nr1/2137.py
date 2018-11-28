#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
char s[200][200],cap[200],last;
int len[200],caplen,capi,bj,capjs[200][200];

int main()
{
	int T,n;
	scanf("%d",&T);
	for (int ri=0;ri<T;ri++)
	{
	/*	if (ri==10)
		{
			bj=bj&1;
		}*/
		scanf("%d",&n);
		bj=0;
		for (int i=0;i<n&&bj==0;i++)
		{			
			scanf("%s",s[i]);
			len[i]=strlen(s[i]);
			if (i==0)
			{
				last=s[i][0];
				capi=0;
				cap[0]=last;
				capjs[i][0]=1;
				caplen=0;
			}
			else
			{
				if (s[i][0]!=cap[0])
				{
					bj=1;
					break;
				}
				else
				{
					last=s[i][0];
					capi=0;
					capjs[i][0]=1;
				}
			}
			for (int j=1;j<len[i]&&bj==0;j++)
			{
				if (i==0)
				{
					if (s[i][j]==last)
					{
						capjs[i][capi]++;
					}
					else
					{
						capi++;
						caplen=capi;
						cap[capi]=s[i][j];
						capjs[i][capi]=1;
						last=s[i][j];
					}					
				}
				else
				{
					if (s[i][j]==last)
					{
						capjs[i][capi]++;
					}
					else
					{
						capi++;
						if (capi>caplen||s[i][j]!=cap[capi])
						{
							bj=1;
							break;
						}
						capjs[i][capi]=1;
						last=s[i][j];
					}
				}				
			}		
			if (capi<caplen)
			{
				bj=1;break;
			}	
		}
		if (bj==1)
		{
			printf("Case #%d: Fegla Won\n",ri+1);
		}
		else
		{
			int sum1,sum2,mid,tmp;
			sum1=0;
			for (int i=0;i<=caplen;i++)
			{
				for (int j=0;j<n;j++)
					for (int k=j;k<n;k++)
						if (capjs[j][i]>capjs[k][i])
						{
							tmp=capjs[j][i];
							capjs[j][i]=capjs[k][i];
							capjs[k][i]=tmp;
						}
				if (n%2==1)
				{
					mid=capjs[n/2][i];
					for (int j=0;j<n;j++)
					{
						sum1+=abs(capjs[j][i]-mid);
					}
				}
				else
				{
					
					mid=(capjs[n/2][i]+capjs[(n/2)-1][i])/2;
					for (int j=0;j<n;j++)
					{
						sum1+=abs(capjs[j][i]-mid);
					}
				}
			}
			printf("Case #%d: %d\n",ri+1,sum1);
		}
	}
}
