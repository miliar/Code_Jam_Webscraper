#include<bits/stdc++.h>
using namespace std;
int stored[1000007];
int flagged[13];
int shutup(int smhs)
{
			int i,rick;
	while(smhs!=0)
	{
			rick=smhs%10;
		flagged[rick]++;
				smhs=smhs/10;
	}
	
}
int FLL(int smhs)
{
	int rick;
	while(smhs!=0)
	{
				rick=smhs%10;
		if(rick!=0)
				return(rick);
			smhs=smhs/10;
		}
}
int main()
{
//	freopen("A-large.in", "r" , stdin);
//	freopen ("oonew2.out","w",stdout);	
	int k,i,smhs,test,	j,p,ans;
				stored[0]=-1;
	for(i=1;i<=1000001;i++)
		{
						for(k=0;k<=10;k++)
				flagged[k]=0;	
			for(j=1;;j++)
				{
					if(!(flagged[0]>=1&&flagged[1]>=1&&flagged[2]>=1&&flagged[3]>=1&&flagged[4]>=1&&flagged[5]>=1&&flagged[6]>=1&&flagged[7]>=1&&flagged[8]>=1&&flagged[9]>=1))
						{
							shutup(i*j);
						}
					if((flagged[0]>=1&&flagged[1]>=1&&flagged[2]>=1&&flagged[3]>=1&&flagged[4]>=1&&flagged[5]>=1&&flagged[6]>=1&&flagged[7]>=1&&flagged[8]>=1&&flagged[9]>=1))
						{
							stored[i]=j;
							break;
						}		
				}
		}
	scanf("%d",&test);
	for(i=1;i<=test;i++)
	{
		scanf("%d",&smhs);
			if(smhs!=0)
					printf("Case #%d: %d\n",i,stored[smhs]*smhs);
				else
					printf("Case #%d: INSOMNIA\n",i);				
	}
//	fclose(stdout);
	return(0);
}

