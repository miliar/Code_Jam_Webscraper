#include<stdio.h>
#include<string.h>
#include<iostream>
int main()
{
	freopen("A-large.in","r",stdin);
   	freopen("output2l.txt","w+",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		char arr[5][5],temp,dia1[6]="....\0",dia2[6]="....\0";
		int dot_count=0,x_win=0,o_win=0;
		for(int j=0;j<4;j++)
		{
			scanf("%s", arr[j]);
			arr[j][4]='\0';

			//Check horizontally
			if((strcmp(arr[j],"XXXX")==0)||(strcmp(arr[j],"TXXX")==0)||(strcmp(arr[j],"XTXX")==0)||(strcmp(arr[j],"XXTX")==0)||(strcmp(arr[j],"XXXT")==0))
			{
				x_win=1;
			}
			if((strcmp(arr[j],"OOOO")==0)||(strcmp(arr[j],"TOOO")==0)||(strcmp(arr[j],"OTOO")==0)||(strcmp(arr[j],"OOTO")==0)||(strcmp(arr[j],"OOOT")==0))
			{
				o_win=1;
			}
		}
		if((o_win==0)&&(x_win==0))
		{
			///Transpose
			for(int k=0;k<4;k++)
			{
				for(int l=k;l<4;l++)
				{
					if((arr[k][l]=='.')||(arr[l][k]=='.'))
					{
						dot_count++;
					}
					temp=arr[k][l];
					arr[k][l]=arr[l][k];
					arr[l][k]=temp;
				}
			}

			//Check vertically
			for(int j=0;j<4;j++)
			{
				if((strcmp(arr[j],"XXXX")==0)||(strcmp(arr[j],"TXXX")==0)||(strcmp(arr[j],"XTXX")==0)||(strcmp(arr[j],"XXTX")==0)||(strcmp(arr[j],"XXXT")==0))
				{
					x_win=1;
					break;
				}
				if((strcmp(arr[j],"OOOO")==0)||(strcmp(arr[j],"TOOO")==0)||(strcmp(arr[j],"OTOO")==0)||(strcmp(arr[j],"OOTO")==0)||(strcmp(arr[j],"OOOT")==0))
				{
					o_win=1;
					break;
				}
			}
			
			//Make diagonals
			for(int k=0;k<4;k++)
			{
				dia1[k]=arr[k][k];
				dia2[k]=arr[3-k][k];
			}

			//Check diagonals
			if((strcmp(dia1,"XXXX")==0)||(strcmp(dia1,"TXXX")==0)||(strcmp(dia1,"XTXX")==0)||(strcmp(dia1,"XXTX")==0)||(strcmp(dia1,"XXXT")==0))
			{
				x_win=1;
			}
			if((strcmp(dia1,"OOOO")==0)||(strcmp(dia1,"TOOO")==0)||(strcmp(dia1,"OTOO")==0)||(strcmp(dia1,"OOTO")==0)||(strcmp(dia1,"OOOT")==0))
			{
				o_win=1;
			}
			if((strcmp(dia2,"XXXX")==0)||(strcmp(dia2,"TXXX")==0)||(strcmp(dia2,"XTXX")==0)||(strcmp(dia2,"XXTX")==0)||(strcmp(dia2,"XXXT")==0))
			{
				x_win=1;
			}
			if((strcmp(dia2,"OOOO")==0)||(strcmp(dia2,"TOOO")==0)||(strcmp(dia2,"OTOO")==0)||(strcmp(dia2,"OOTO")==0)||(strcmp(dia2,"OOOT")==0))
			{
				o_win=1;
			}
		}

		if(x_win==1)
		{
		printf("Case #%d: X won\n",i);					
		}
		else if(o_win==1)
		{
		printf("Case #%d: O won\n",i);					
		}
		else if(dot_count!=0)
		{
		printf("Case #%d: Game has not completed\n",i);
		}
		else
		{
		printf("Case #%d: Draw\n",i);
		}	
	}	
   	fclose (stdout);
	fclose (stdin);
	return 0;
}
