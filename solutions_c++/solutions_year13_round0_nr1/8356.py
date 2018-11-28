#include"iostream.h"
#include"stdio.h"
#include"conio.h"

void main()
{
	clrscr();
	FILE *fp;
	fp=fopen("output.txt","w");
	int i,j,flag=0,countx=0,counto=0,win=0,ch=1,empty=0,n,m=1;
	char tictac[4][4];
	cin>>n;
	while(m<=n)
	{
	fprintf(fp,"\n\n");
	cout<<"\n\n";
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			cin>>tictac[i][j];
		}
	}
	while(1)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(tictac[i][j]=='x')
				{
					countx++;
				}
				if(tictac[i][j]=='o')
				{
					counto++;
				}
				if(tictac[i][j]=='t')
				{
					flag=1;
				}
				if(tictac[i][j]=='.')
				{
					empty++;
				}
			}
			if((flag+countx)==4)
			{
				fprintf(fp,"Case #%d: X won",m);
				win=1;
				break;
			}
			if((flag+counto)==4)
			{
				fprintf(fp,"Case #%d: O won",m);
				win=1;
				break;
			}
			flag=0;
			countx=0;
			counto=0;
		}
		if(win==1)
		{
			break;
		}
		for(j=0;j<4;j++)
		{
			for(i=0;i<4;i++)
			{
				if(tictac[i][j]=='x')
				{
					countx++;
				}
				if(tictac[i][j]=='o')
				{
					counto++;
				}
				if(tictac[i][j]=='t')
				{
					flag=1;
				}
			}
			if((flag+countx)==4)
			{
				fprintf(fp,"Case #");
				fprintf(fp,"%d",m);
				fprintf(fp,": X won");
				win=1;
				break;
			}
			if((flag+counto)==4)
			{
				fprintf(fp,"Case #%d: O won",m);
				win=1;
				break;
			}
			flag=0;
			countx=0;
			counto=0;
		}
		if(win==1)
		{
			break;
		}
		flag=0;
		countx=0;
		counto=0;
		for(i=0;i<4;i++)
		{
			j=i;
				if(tictac[i][j]=='x')
				{
					countx++;
				}
				if(tictac[i][j]=='o')
				{
					counto++;
				}
				if(tictac[i][j]=='t')
				{
					flag=1;
				}
		}
			if((flag+countx)==4)
			{
				fprintf(fp,"Case #%d: X won",m);
				break;
			}
			if((flag+counto)==4)
			{
				fprintf(fp,"Case #%d: O won",m);
				break;
			}
			flag=0;
			countx=0;
			counto=0;
		for(i=0,j=3;i<4;i++,j--)
		{
				if(tictac[i][j]=='x')
				{
					countx++;
				}
				if(tictac[i][j]=='o')
				{
					counto++;
				}
				if(tictac[i][j]=='t')
				{
					flag=1;
				}
		}
			if((flag+countx)==4)
			{
				fprintf(fp,"Case #%d: X won",m);
				break;
			}
			if((flag+counto)==4)
			{
				fprintf(fp,"Case #%d: O won",m);
				break;
			}
		if(empty>0)
		{
			fprintf(fp,"Case #%d: Game has not completed",m);
			break;
		}
		cout<<m;
		fprintf(fp,"Case #");
		fprintf(fp,"%d",m);
		fprintf(fp,": Draw");
		break;
	}
	m++;
	}
	fclose(fp);
	getch();
}
