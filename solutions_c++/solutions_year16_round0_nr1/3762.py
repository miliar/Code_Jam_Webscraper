#include<stdio.h>
int store[1000007];
int flagi[13];
int maini(int N)
{
	int i,num;
	while(N!=0)
	{
		num=N%10;
		flagi[num]++;
		N=N/10;
	}
}
int main()
{
//	freopen("A-large.in", "r" , stdin);
//	freopen ("shivangoutput1.out","w",stdout);
	int k,i,N,T,j,p;
	store[0]=-1;
	for(i=1;i<=1000001;i++)
		{
			for(k=0;k<=10;k++)
				flagi[k]=0;			
			for(j=1;;j++)
				{
					if(!(flagi[0]>=1&&flagi[1]>=1&&flagi[2]>=1&&flagi[3]>=1&&flagi[4]>=1&&flagi[5]>=1&&flagi[6]>=1&&flagi[7]>=1&&flagi[8]>=1&&flagi[9]>=1))
						{
							maini(i*j);
						}
					if((flagi[0]>=1&&flagi[1]>=1&&flagi[2]>=1&&flagi[3]>=1&&flagi[4]>=1&&flagi[5]>=1&&flagi[6]>=1&&flagi[7]>=1&&flagi[8]>=1&&flagi[9]>=1))
						{
							store[i]=j;
							break;
						}
				}
		}
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d",&N);
			if(N!=0)
					printf("Case #%d: %d\n",i,store[N]*N);
				else
					printf("Case #%d: INSOMNIA\n",i);			
	}	
//	fclose(stdout);	
	return(0);
}


