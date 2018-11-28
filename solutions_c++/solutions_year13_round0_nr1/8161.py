// Tic-Tac.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
    int T,i,j,c,k;
	char a[4][4];
	FILE *fi,*fo;
	fi=fopen("input.txt","r");
	fo=fopen("output.txt","w");
	fscanf(fi,"%d",&T);
	for(i=1;i<=T;i++)
	{
		c=0;
		for(j=0;j<4;j++)
		{
			fscanf(fi,"%c %c %c %c",&a[j][0],&a[j][1],&a[j][2],&a[j][3]);
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(j==k==0)
				{
					if(a[j][k]==a[j][k+1]==a[j][k+2]==a[j][k+3]=='X')
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j][k+1]==a[j][k+2]==a[j][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k+1]=='T' && (a[j][k]==a[j][k+2]==a[j][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k+2]=='T' && (a[j][k]==a[j][k+1]==a[j][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k+3]=='T' && (a[j][k]==a[j][k+1]==a[j][k+2]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
                    if(a[j][k]==a[j][k+1]==a[j][k+2]==a[j][k+3]=='Y')
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j][k+1]==a[j][k+2]==a[j][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k+1]=='T' && (a[j][k]==a[j][k+2]==a[j][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k+2]=='T' && (a[j][k]==a[j][k+1]==a[j][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k+3]=='T' && (a[j][k]==a[j][k+1]==a[j][k+2]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}

                    if(a[j][k]==a[j+1][k]==a[j+2][k]==a[j+3][k]=='X')
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j+1][k]==a[j+2][k]==a[j+3][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+1][k]=='T' && (a[j][k]==a[j+2][k]==a[j+3][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+2][k]=='T' && (a[j][k]==a[j+1][k]==a[j+3][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+3][k]=='T' && (a[j][k]==a[j+1][k]==a[j+2][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
                    if(a[j][k]==a[j+1][k]==a[j+2][k]==a[j+3][k]=='Y')
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j+1][k]==a[j+2][k]==a[j+3][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+1][k]=='T' && (a[j][k]==a[j+2][k]==a[j+3][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+2][k]=='T' && (a[j][k]==a[j+1][k]==a[j+3][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+3][k]=='T' && (a[j][k]==a[j+1][k]==a[j+2][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}

                    if(a[j][k]==a[j+1][k+1]==a[j+2][k+2]==a[j+3][k+3]=='X')
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j+1][k+1]==a[j+2][k+2]==a[j+3][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+1][k+1]=='T' && (a[j][k]==a[j+2][k+2]==a[j+3][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+2][k+2]=='T' && (a[j][k]==a[j+1][k+1]==a[j+3][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+3][k+3]=='T' && (a[j][k]==a[j+1][k+1]==a[j+2][k+2]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
                    if(a[j][k]==a[j+1][k+1]==a[j+2][k+2]==a[j+3][k+3]=='Y')
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j+1][k+1]==a[j+2][k+2]==a[j+3][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+1][k+1]=='T' && (a[j][k]==a[j+2][k+2]==a[j+3][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+2][k+2]=='T' && (a[j][k]==a[j+1][k+1]==a[j+3][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+3][k+3]=='T' && (a[j][k]==a[j+1][k+1]==a[j+2][k+2]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
				}
				if(j<k)
				{
                    if(a[j][k]==a[j+1][k]==a[j+2][k]==a[j+3][k]=='X')
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j+1][k]==a[j+2][k]==a[j+3][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+1][k]=='T' && (a[j][k]==a[j+2][k]==a[j+3][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+2][k]=='T' && (a[j][k]==a[j+1][k]==a[j+3][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j+3][k]=='T' && (a[j][k]==a[j+1][k]==a[j+2][k]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
                    if(a[j][k]==a[j+1][k]==a[j+2][k]==a[j+3][k]=='Y')
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j+1][k]==a[j+2][k]==a[j+3][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+1][k]=='T' && (a[j][k]==a[j+2][k]==a[j+3][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+2][k]=='T' && (a[j][k]==a[j+1][k]==a[j+3][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j+3][k]=='T' && (a[j][k]==a[j+1][k]==a[j+2][k]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
				}
				if(j>k)
				{
                    if(a[j][k]==a[j][k+1]==a[j][k+2]==a[j][k+3]=='X')
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j][k+1]==a[j][k+2]==a[j][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k+1]=='T' && (a[j][k]==a[j][k+2]==a[j][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k+2]=='T' && (a[j][k]==a[j][k+1]==a[j][k+3]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
					if(a[j][k+3]=='T' && (a[j][k]==a[j][k+1]==a[j][k+2]=='X'))
					{
						fprintf(fo,"Case #%d: X won",i);
						c=1;
						//break;
					}
                    if(a[j][k]==a[j][k+1]==a[j][k+2]==a[j][k+3]=='Y')
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k]=='T' && (a[j][k+1]==a[j][k+2]==a[j][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k+1]=='T' && (a[j][k]==a[j][k+2]==a[j][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k+2]=='T' && (a[j][k]==a[j][k+1]==a[j][k+3]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
					if(a[j][k+3]=='T' && (a[j][k]==a[j][k+1]==a[j][k+2]=='Y'))
					{
						fprintf(fo,"Case #%d: Y won",i);
						c=1;
						//break;
					}
				}
			    if(c==1)
			    {
					//break;
				}
			}
			if(c==1)
			{
				//break;
			}
		}
		if(c==1)
			//break;
        if(a[0][3]==a[1][2]==a[2][1]==a[3][0]=='X')
		{
			fprintf(fo,"Case #%d: X won",i);
			c=1;
			//break;
   		}
		if(a[0][3]=='T' && (a[1][2]==a[2][1]==a[3][0]=='X'))
		{
			fprintf(fo,"Case #%d: X won",i);
			c=1;
			//break;
		}
		if(a[1][2]=='T' && (a[0][3]==a[2][1]==a[3][0]=='X'))
		{
			fprintf(fo,"Case #%d: X won",i);
			c=1;
			//break;
		}
		if(a[2][1]=='T' && (a[0][3]==a[1][2]==a[3][0]=='X'))
		{
			fprintf(fo,"Case #%d: X won",i);
			c=1;
			//break;
		}
		if(a[3][0]=='T' && (a[0][3]==a[1][2]==a[2][1]=='X'))
		{
			fprintf(fo,"Case #%d: X won",i);
			c=1;
			//break;
		}
		if(a[0][3]==a[1][2]==a[2][1]==a[3][0]=='Y')
		{
			fprintf(fo,"Case #%d: Y won",i);
			c=1;
			//break;
		}
		if(a[0][3]=='T' && (a[1][2]==a[2][1]==a[3][0]=='Y'))
		{
			fprintf(fo,"Case #%d: Y won",i);
			c=1;
			//break;
		}
		if(a[1][2]=='T' && (a[0][3]==a[2][1]==a[3][0]=='Y'))
		{
			fprintf(fo,"Case #%d: Y won",i);
			c=1;
			//break;
		}
		if(a[2][1]=='T' && (a[0][3]==a[1][2]==a[3][0]=='Y'))
		{
			fprintf(fo,"Case #%d: Y won",i);
			c=1;
			//break;
		}
		if(a[3][0]=='T' && (a[0][3]==a[1][2]==a[2][1]=='Y'))
		{
			fprintf(fo,"Case #%d: Y won",i);
			c=1;
			//break;
		}
		if(c==0)
		{
			for(j=0;j<4;j++)
			{
				for(k=0;k<4;k++)
				{
					if(c==0)
					{
						if(a[j][k]=='.')
						{
							fprintf(fo,"Case #%d: Game has not completed",i);
							c=1;
						//break;
						}
					}
				}
			}
		}
		if(c==0)
		{
			fprintf(fo,"Case #%d: Draw",i);
			c=1;
			//break;
		}
	    //continue;
	}
	fclose(fi);
	fclose(fo);
	return 0;
}

