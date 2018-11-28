#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>

int X,R,C;
int logic()
{
	if(X<=2)
	{
		if(X==2&&R==1&&C==1||X==2&&R==1&&C==3||X==2&&R==3&&C==1||X==2&&R==3&&C==3)
		return  0;
		else
		return 1;
	}
	else
	{
		if(X==3&&R==2&&C==3||
		   X==3&&R==3&&C==2||
		   X==3&&R==3&&C==3||
		   X==3&&R==3&&C==4||
		   X==3&&R==4&&C==3||
		   X==4&&R==3&&C==4||
		   X==4&&R==4&&C==3||
		   X==4&&R==4&&C==4
		   )
		   return 1;
		   else
		   return 0;
	}
}
void inputoutput(char inputfile[],char outputfile[])
{
	FILE *f1,*f2;
	f1=fopen(inputfile,"r");
	f2=fopen(outputfile,"w");
	int no_case,count=0;
	fscanf(f1,"%d",&no_case);
	for(int i=1;i<=no_case;i++)
	{
	  fprintf(f2,"Case #%d: ",i);
	  fscanf(f1,"%d%d%d",&X,&R,&C) ;
	  int flag=logic();
	  if(flag==0)
	  {fprintf(f2,"RICHARD\n");
	  count++;
	  }
	  else
	  fprintf(f2,"GABRIEL\n");
	}
	printf("%d",count);
}
void main()
{
	 char inputfile[]="input.txt";
	char outputfile[]="output.txt";
	clrscr();
	inputoutput(inputfile,outputfile);
	getch();
}