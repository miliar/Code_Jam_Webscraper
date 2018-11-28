#include<iostream>
using namespace std;

int main()
{
	FILE *in,*out;
	in=fopen("A-large.in","r");
	out=fopen("Al.out","w");
	int T;
	int brd[4][4]={0};
	char s[5];
	int row=0,col=0,dia1=0,dia2=0;
	bool check0=0;
	fscanf(in,"%d",&T);
	for(int i=0;i<T;i++)
	{
		
		for(int j=0;j<4;j++)
		{
			fscanf(in,"%s",s);
			for(int k=0;k<4;k++)
			{
				if(s[k]=='X')brd[j][k]=3;
				if(s[k]=='O')brd[j][k]=5;
				if(s[k]=='T')brd[j][k]=23;
				if(s[k]=='.')check0=1;
			}
		}

		for(int j=0;j<4;j++)
		{
			row=0;
			col=0;
			for(int k=0;k<4;k++)
			{
				row += brd[j][k];
				col += brd[k][j];
				
			}
			dia1+=brd[j][j];
			dia2+=brd[j][3-j];
			if(row==12 || col==12 || row==32 || col==32 || dia1==12 || dia1==32 || dia2==12 || dia2==32) { fprintf(out,"Case #%d: X won\n",i+1); break; }
			if(row==20 || col==20 || row==38 || col==38 || dia2==20 || dia2==38 || dia1==20 || dia1==38) { fprintf(out,"Case #%d: O won\n",i+1); break; }
			row=100;
		}

		if(row==100 && check0) fprintf(out,"Case #%d: Game has not completed\n",i+1);
		if(row==100 && check0==0) fprintf(out,"Case #%d: Draw\n",i+1);
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				brd[i][j]=0;
		check0=0;
		dia1=0;
		dia2=0;
	
	
	}

	fclose(in);
	fclose(out);
	return 0;
}