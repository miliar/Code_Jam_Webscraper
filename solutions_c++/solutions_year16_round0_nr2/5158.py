#include<bits/stdc++.h>
using namespace std;
char mind[109];
int sum;
char xxx(char ch)
{
				if(ch=='+')
		return('-');
	else
				return('+');
}
void mymind(int L,int R)
{
			int i=L,j=R;
	char hell;
	while(i<=j)
		{
				hell=mind[i];
			mind[i]=			xxx(mind[j]);
			mind[j]=		xxx(hell);			
			i++;
			j--;
		}	
}
int whatsup()
{
	int i;
	for(i=0;i<=sum-1; 	i++)
		{
			if(mind[i]=='-')
						return(0);
		}		
	return(1);
}
int rmn()
{
				int i;
	for(i=sum-1;i>=0;i--)
		{
			if(mind[i]=='-')
				return(i);
		}	
	return(-1);
}
		int lmn()
		{
			int i;
		for(i=0;i<=sum-1;i++)
		{
			if(mind[i]=='-')
						return(i);
		}	
	return(-1);
}	
int main()
{
//freopen("B-large.in", "r" , stdin);
//freopen ("output2.out","w",stdout);
	int i,T,hey,rhs,lhs;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
		{
					hey=0;
				scanf("%s",mind);
			sum=strlen(mind);
			while(1)
				{
					if(whatsup()==1)
						break;
						rhs=rmn();
						lhs=lmn();	
					if(lhs>0)
						{	mymind(0,lhs-1);
							hey++;	
						}					
									if(whatsup()==1)
						break;
					mymind(0,rhs);
					hey++;
				}
			printf("Case #%d: %d\n",i,hey);
		}
//	fclose(stdout);
	return(0);
}

