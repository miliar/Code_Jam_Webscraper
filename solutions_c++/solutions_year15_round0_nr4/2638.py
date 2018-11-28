#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	FILE *ftr;
	FILE *ftr1;
	ftr=fopen("input.in","r");
	ftr1=fopen("output.txt","w");
	fscanf(ftr,"%d",&t);

	for(int j=1;j<=t;j++)
	{
		int x,r,c;
		fscanf(ftr,"%d%d%d",&x,&r,&c);
		int r1=min(r,c);
		int c1=max(r,c);

		if(x==1)
		{
			fprintf(ftr1,"Case #%d: GABRIEL\n",j);
		}
		else if(x==2)
		{
			if(r1==1 && c1==1)
			{
				fprintf(ftr1,"Case #%d: RICHARD\n",j);
			}
			else if(r1==1 && c1==3)
			{
				fprintf(ftr1,"Case #%d: RICHARD\n",j);
			}
			else if(r1==3 && c1==3)
			{
				fprintf(ftr1,"Case #%d: RICHARD\n",j);
			}
			else
			{
				fprintf(ftr1,"Case #%d: GABRIEL\n",j);
			}
		}
		else if(x==3)
		{
			if(r1==2 && c1==3)
			{
				fprintf(ftr1,"Case #%d: GABRIEL\n",j);
			}
			else if(r1==3 && c1==3)
			{
				fprintf(ftr1,"Case #%d: GABRIEL\n",j);
			}
			else if(r1==3 && c1==4)
			{
				fprintf(ftr1,"Case #%d: GABRIEL\n",j);
			}
			else
			{
				fprintf(ftr1,"Case #%d: RICHARD\n",j);
			}
		}
		else if(x==4)
		{
			if(r1==3 && c1==4)
			{
				fprintf(ftr1,"Case #%d: GABRIEL\n",j);
			}
			else if(r1==4 && c1==4)
			{
				fprintf(ftr1,"Case #%d: GABRIEL\n",j);
			}
			else 
			{
				fprintf(ftr1,"Case #%d: RICHARD\n",j);
			}
		}
	}
return 0;}