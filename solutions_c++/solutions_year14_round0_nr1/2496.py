#include<stdio.h>

FILE *in=fopen("1.in","r");
FILE *out=fopen("1.out","w");

int TT,Tcnt;
int R1,R2;
int Data1[5][5];
int Data2[5][5],Ans[100],Idx=0;

int main()
{
	int i,j;
	fscanf(in,"%d",&TT);
	for(Tcnt=1;Tcnt<=TT;Tcnt++)
	{
		Idx=0;
		fscanf(in,"%d",&R1);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)fscanf(in,"%d",&Data1[i][j]);
		}
		fscanf(in,"%d",&R2);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)fscanf(in,"%d",&Data2[i][j]);
		}
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(Data1[R1][i]==Data2[R2][j])Ans[++Idx]=Data2[R2][j];
			}
		}
		if(Idx==1)fprintf(out,"Case #%d: %d\n",Tcnt,Ans[Idx]);
		else if(Idx>1)fprintf(out,"Case #%d: Bad magician!\n",Tcnt);
		else fprintf(out,"Case #%d: Volunteer cheated!\n",Tcnt);
	}
	return 0;
}