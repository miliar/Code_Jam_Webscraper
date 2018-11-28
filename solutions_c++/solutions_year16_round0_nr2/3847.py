#include<stdio.h>
#include<string.h>

char str[109];
int len;

char flipsymbol(char ch)
{
	if(ch=='+')
		return('-');
	else
		return('+');
}

void reversei(int L,int R)
{
	int i=L,j=R;
	char temp;
	
	while(i<=j)
		{
			temp=str[i];
			str[i]=flipsymbol(str[j]);
			str[j]=flipsymbol(temp);			
			i++;
			j--;
		}
	
}

int checki()
{
	int i;
	
	for(i=0;i<=len-1;i++)
		{
			if(str[i]=='-')
				return(0);
		}	
		
	return(1);
}

int rightmostneg()
{
	int i;
	
	for(i=len-1;i>=0;i--)
		{
			if(str[i]=='-')
				return(i);
		}	
	return(-1);
}

int leftmostneg()
{
	int i;
	
	for(i=0;i<=len-1;i++)
		{
			if(str[i]=='-')
				return(i);
		}	
	return(-1);
}

int main()
{
//freopen("B-large.in", "r" , stdin);
//freopen ("output2.out","w",stdout);

	
	int i,T,counti,rightneg,leftneg;
	scanf("%d",&T);
	
	for(i=1;i<=T;i++)
		{
			counti=0;
			scanf("%s",str);
	
			len=strlen(str);
			
			while(1)
				{
					if(checki()==1)
						break;
						
					rightneg=rightmostneg();
					leftneg=leftmostneg();
					
				//		printf("leftneg=%d and rightneg=%d\n",leftneg,rightneg);
								
					if(leftneg>0)
						{
				//			printf("Hello1");
							reversei(0,leftneg-1);
							counti++;	
						}
						
					if(checki()==1)
						break;
					
					reversei(0,rightneg);
				//	printf("%s\n",str);
					counti++;
				}
			
			printf("Case #%d: %d\n",i,counti);
			
		}
	
	
	
//	fclose(stdout);
	
	return(0);
}



