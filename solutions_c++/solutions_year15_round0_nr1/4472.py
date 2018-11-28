#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>

int smax,shy[1000]  ;
int logic()
{
	int noofpersonstandup=shy[0];
	int nooffriendneed=0;

	for(int i=1;i<=smax;i++)
	{
		if(shy[i]==0||noofpersonstandup>=i)
		{
			noofpersonstandup+=shy[i];
		}
		else
		{
			int t=i-noofpersonstandup;
			nooffriendneed+=t;
			noofpersonstandup+=shy[i]+t;
		}
	}
	return nooffriendneed ;
}
void inputoutput(char inputfile[],char outputfile[])
{
	FILE *f1,*f2;
	f1=fopen(inputfile,"r");
	f2=fopen(outputfile,"w");
	int no_case,j;
	char ch;
	fscanf(f1,"%d",&no_case);
	for(int i=1;i<=no_case;i++)
	{
		smax=0;
	  fprintf(f2,"case #%d: ",i);
	  fscanf(f1,"%d",&smax) ;
	  fscanf(f1,"%c",&ch) ;
	  for(j=0;j<=smax;j++)
	  {
	      fscanf(f1,"%c",&ch);
	      shy[j]=ch-48;
	  }
	  /*
	  for(j=0;j<=smax;j++)
	  {
		printf("%d ",shy[j]);
	  }
	  */
	  fscanf(f1,"%c",&ch) ;
	  //printf("%d\n",logic());
	  fprintf(f2,"%d\n",logic());
	}
}
void main()
{
	 char inputfile[]="input.txt";
	char outputfile[]="output.txt";
	clrscr();
	inputoutput(inputfile,outputfile);
	getch();
}