#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

int L,X;
int i=0,j=0;
int input[10000];
int matrix[][4]={1,2,3,4,
		2,-1,4,-3,
		3,-4,-1,2,
		4,3,-2,-1};
int multiply(int a,int b)
{
	if(a>0&&b>0||a<0&&b<0)
	return matrix[abs(a)-1][abs(b)-1];
	else
	return -1*matrix[abs(a)-1][abs(b)-1];
}

int getvariable(int loction)
{
	int j=loction%L;
	return input[j];
}

int logic()
{
	int i,j,k,current,f1=0,f3=0;
	current=1;
	for( i=0;i<L*X;i++)
	{
		current=multiply(current,getvariable(i));
		if(current==2)
		{
			f1=1;
			i++;
			break;
		}
	}
	current=1;
	for(j=L*X-1;j>i;j--)
	{
		current=multiply(getvariable(j),current);
		if(current==4)
		{
			f3=1;
			j--;
			break;
		}
	}
	current=1;
	for(k=i;k<=j;k++)
	{
		current=multiply(current,getvariable(k));
	}
	if(current==3&&k-1==j&&f1==1&&f3==1)
	{
		return 1;
	}
	else
	return 0;
}
void inputoutput(char inputfile[],char outputfile[])
{
	FILE *f1,*f2;
	f1=fopen(inputfile,"r");
	f2=fopen(outputfile,"w");
	int no_case;
	char string[10000];
	fscanf(f1,"%d",&no_case);
	for(int k=1;k<=no_case;k++)
	{
		i=0;j=0;
		fprintf(f2,"Case #%d: ",k);
		fscanf(f1,"%d%d",&L,&X);
		fscanf(f1,"%s",string);
		for(int lj=0;lj<L;lj++)
		{
			switch(string[lj])
			{
				case 'i':input[lj]=2;break;
				case 'j':input[lj]=3;break;
				case 'k':input[lj]=4;break;
			}
		}

		int flag=logic();
		/*printf("L %d X %d string=%s flag=%d\n",L,X,string,flag) ;
		for(i=0;i<L;i++)
		printf("%d",input[i]);
		printf("\n");*/
		if(flag==0)
		fprintf(f2,"NO\n");
		else
		fprintf(f2,"YES\n");
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