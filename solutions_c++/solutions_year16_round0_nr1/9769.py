#include<stdio.h>

int T;
int N;
int main(void)
{
	FILE *fi,*fo;
	fi = fopen("input.txt","r");
	fo = fopen("output.txt","w");

	fscanf(fi,"%d",&T);
	int testcase;
	int number[14];
	int init;
	int i,iN;
	int check;
	for(testcase=1;testcase<=T;testcase++)
	{
		fscanf(fi,"%d",&N);
		if(N!=0)
		{
			for(init=0;init<10;init++) number[init]=0;
			check=0;
			for(i=1;;i++)
			{
				iN = i*N;
				//printf("*iN = %d\n",iN);
				while(iN>0)
				{
					//printf(" iN = %d\n",iN);
					if(number[iN%10]==0) check++;
					number[iN%10]=1;
					iN/=10;
				}
				if(check==10) break;
			}
			fprintf(fo,"Case #%d: %d\n",testcase,i*N);
		}
		else//N==0
		{
			fprintf(fo,"Case #%d: INSOMNIA\n",testcase);
		}
		
	}
}