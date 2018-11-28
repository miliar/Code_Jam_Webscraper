#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>

int precomp[1000007];

int marki[13];

int findlast(int N)
{
	int temp;
	
	while(N!=0)
	{
		temp=N%10;
		if(temp!=0)
			return(temp);
		N=N/10;
	}
}

int digiti(int N)
{
	int i,temp;
	

	while(N!=0)
	{
		temp=N%10;
		marki[temp]++;
		N=N/10;
	}
	
}
 

int main()
{
//	freopen("A-large.in", "r" , stdin);
//	freopen ("oonew2.out","w",stdout);

	
	int k,i,N,T,j,p,ans;
	precomp[0]=-1;
	
	
	for(i=1;i<=1000001;i++)
		{
			for(k=0;k<=10;k++)
				marki[k]=0;	
				
			for(j=1;;j++)
				{
					if(!(marki[0]>=1&&marki[1]>=1&&marki[2]>=1&&marki[3]>=1&&marki[4]>=1&&marki[5]>=1&&marki[6]>=1&&marki[7]>=1&&marki[8]>=1&&marki[9]>=1))
						{
							digiti(i*j);
						}
					if((marki[0]>=1&&marki[1]>=1&&marki[2]>=1&&marki[3]>=1&&marki[4]>=1&&marki[5]>=1&&marki[6]>=1&&marki[7]>=1&&marki[8]>=1&&marki[9]>=1))
						{
							precomp[i]=j;
							break;
						}
				/*	else
						{
							precomp[i]=j-1;
							break;
						}
				*/		
				}
		}
	/*
		printf("Printing precomp array-->\n");
	for(i=1;i<=1000000;i++)
		{
			printf("%d-%d\n",i,precomp[i]);
		}
	*/
	scanf("%d",&T);

	for(i=1;i<=T;i++)
	{
		scanf("%d",&N);
		
	/*	if(N<10)
			{
				if(N!=0)
					printf("Case #%d: %d\n",i,precomp[N]*N);
				else
					printf("Case #%d: INSOMNIA\n",i);
			}
			
		else
			{
				p=findlast(N);
				
					for(k=0;k<=10;k++)
							marki[k]=0;	
				
						for(j=1;j<=precomp[p];j++)
						{
						if(!(marki[0]>=1&&marki[1]>=1&&marki[2]>=1&&marki[3]>=1&&marki[4]>=1&&marki[5]>=1&&marki[6]>=1&&marki[7]>=1&&marki[8]>=1&&marki[9]>=1))
							{
								digiti(N*j);
							}
						
						if((marki[0]>=1&&marki[1]>=1&&marki[2]>=1&&marki[3]>=1&&marki[4]>=1&&marki[5]>=1&&marki[6]>=1&&marki[7]>=1&&marki[8]>=1&&marki[9]>=1))
						{
							ans=j;
							//precomp[i]=j;
							break;
						}
						
						}
						
							printf("Case #%d: %d\n",i,ans*N);
	*/
			
			if(N!=0)
					printf("Case #%d: %d\n",i,precomp[N]*N);
				else
					printf("Case #%d: INSOMNIA\n",i);
						
				
	}
	
//	fclose(stdout);
	
	return(0);
}


