#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>

int checkwin(char square[])
{
	if (square[1] == square[2] && square[2] == square[3] && square[3] == square[4])
	{
		if(square[1]=='X')
			return 1;
		if(square[1]=='O')
			return 0;
	}
	else if (square[5] == square[6] && square[6] == square[7] && square[7] == square[8])
	{
		if(square[5]=='X')
			return 1;
		if(square[5]=='O')
			return 0;
	}
	else if (square[9] == square[10]&& square[10] == square[11]&& square[11] == square[12])
	{
		if(square[9]=='X')
			return 1;
		if(square[9]=='O')
			return 0;
	}	else if (square[13] == square[14] && square[14] == square[15]&& square[15] == square[16])
	{
		if(square[13]=='X')
			return 1;
		if(square[13]=='O')
			return 0;
	}
	else if (square[1] == square[5] && square[5] == square[9] && square[9] == square[13])
	{
		if(square[1]=='X')
			return 1;
		if(square[1]=='O')
			return 0;
	}
	else if (square[2] == square[6] && square[6] == square[10] && square[10] == square[14])
	{
		if(square[2]=='X')
			return 1;
		if(square[2]=='O')
			return 0;
	}
	else if (square[3] == square[7] && square[7] == square[11] && square[11] == square[15])
	{
		if(square[3]=='X')
			return 1;
		if(square[3]=='O')
			return 0;
	}
	else if (square[4] == square[8] && square[8] == square[12] && square[12] == square[16])
	{
		if(square[4]=='X')
			return 1;
		if(square[4]=='O')
			return 0;
	}
	else if (square[1] == square[6] && square[6] == square[11] && square[11] == square[16])
	{
		if(square[1]=='X')
			return 1;
		if(square[1]=='O')
			return 0;
	}
	else if (square[4] == square[7] && square[7] == square[10] && square[10] == square[13])
	{
		if(square[4]=='X')
			return 1;
		if(square[4]=='O')
			return 0;
	}
	else if(square[1]!='.' && square[2]!='.' && square[3]!='.' && square[4]!='.' && square[5]!='.' && square[6]!='.' && square[7]!='.' && square[8]!='.' && square[9]!='.' && square[10]!='.' && square[12]!='.' && square[13]!='.' && square[14]!='.' && square[15]!='.' && square[16]!='.' && square[17]!='.' )
	{
		return 2;
	}
	return -1;
}

void main()
{
	//square[17]={'.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',}
	clrscr();
	char c;
	char square1[17],square[17];
	for(int j=0;j<17;j++)
	{
		square[j]='.';
		square1[j]='.';
	}
	int no=0;
	int r=1;
	FILE *fp=fopen("in.txt","r");
	FILE *fo=fopen("ou.txt","a");
	fscanf(fp,"%d",&no);
	while(r!=no+1)
       {
	for(int i=1;i<17;i++)
	{
		fscanf(fp,"%c",&c);
		cout<<c;
		if(c=='\n')
		{   fscanf(fp,"%c",&c);
			cout<<c;
		}
		if(c!='T')
		{
			square[i]=c;
			square1[i]=c;
		}
		else if(c=='T')
		{
			square[i]='X';
			square1[i]='O';
		}
	}
	int x=5;
	fscanf(fp,"%c",&c);
      //	square[17]={'x','x','x','x','o','o','x','o','.','.','.','.','.','.','.','.','.',}
	 x=checkwin(square);
	 int y=5;
	 y=checkwin(square1);
	 cout<<"y="<<y<<endl;
	 cout<<"x="<<x;
	fprintf(fo,"%s%d: ","Case #",r);
	if(x==0|| y==0)
		fprintf(fo,"%s\n","O won");
	else if(x==1 || y==1)
		fprintf(fo,"%s\n","X won");
	else if(x==2 || y==2)
		fprintf(fo,"%s\n","Draw");
	else if(x==-1 || y==-1)
		fprintf(fo,"%s\n","Game has not completed");
	r++;
       }
	 fclose(fp);
	 fclose(fo);
	 getch();
}