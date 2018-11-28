#include <bits/stdc++.h>

using namespace std;

int main()
{
	int cases;
	FILE *ftr;
	FILE *ftr1;
	ftr=fopen("input.in","r");
	ftr1=fopen("output.txt","w");
	fscanf(ftr,"%d",&cases);

	for(int t=1;t<=cases;t++)
	{
		int x,r,c;
		//printf("%d\n",t);
		fscanf(ftr,"%d%d%d",&x,&r,&c);

		fprintf(ftr1,"Case #%d: ",t);

		if(x==1)
		{
			fprintf(ftr1,"GABRIEL\n");
		}
		else if(x==2)
		{
			if((r==3 && c==3) || (r==1 && c==1) || (r==1 && c==3) || (r==3 && c==1))
			{
				fprintf(ftr1,"RICHARD\n");
			}
			else
			{
				fprintf(ftr1,"GABRIEL\n");
			}
		}
		else if(x==3)
		{
			if((r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3) || (r==2 && c==3) || (r==3 && c==2))
			{
				fprintf(ftr1,"GABRIEL\n");
			}
			else
			{
				fprintf(ftr1,"RICHARD\n");
			}
		}
		else if(x==4)
		{
			if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))
			{
				fprintf(ftr1,"GABRIEL\n");
			}
			else
			{
				fprintf(ftr1,"RICHARD\n");
			}
		}
	}
return 0;}