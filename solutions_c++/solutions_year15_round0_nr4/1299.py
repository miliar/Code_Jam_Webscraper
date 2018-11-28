#include<stdio.h>
#include<queue>

using namespace std;
int F[1005];
int main()
{
	FILE *in=fopen("1.in","r");
	FILE *out=fopen("1.out","w");
	int TT;
	int X,R,C;
	fscanf(in,"%d",&TT);
	for(int t=1;t<=TT;t++)
	{
		bool flag=0;
		fscanf(in,"%d %d %d",&X,&R,&C);
		if(X==1)flag=0;
		if(X==2)
		{
			if(R*C%2==0)
			{
				flag=0;
			}
			else flag=1;
		}
		if(X==3)
		{
			if(R>=2 && C>=2 && (R*C)%3==0)flag=0;
			else flag=1;
		}
		if(X==4)
		{
			if(R>=3 && C>=3 && (R*C)%4==0)flag=0;
			else flag=1;
		}
		if(flag==0)fprintf(out,"Case #%d: GABRIEL\n",t);
		else fprintf(out,"Case #%d: RICHARD\n",t);
	}
}