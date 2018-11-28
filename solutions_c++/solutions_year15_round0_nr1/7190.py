#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>

using namespace std;

int main()
{
int Tmax=0,Tcount=0;
scanf("%d\n",&Tmax);

int size=1010;
//int size=10;


while(Tcount<Tmax)
	{
	int SI[size],I=0;
	int min=0,mintemp=0;
	int Smax=0,sum=0;
	scanf("%d ",&Smax);
	
	for(I=0;I<=Smax;I++)
		{int ch=getchar_unlocked()-'0';
		//printf("----%d\n",ch);
		if(ch!=0)
			{
			if(sum>=I)
				{sum=sum+ch;}
			else 	{mintemp=I-sum;
				min=min+mintemp;
				sum=sum+ch+mintemp;
				}	
			}	
		}
	scanf("\n");
	Tcount++;
	printf("Case #%d: %d\n",Tcount,min);
	
		}
	

return 0;
}
