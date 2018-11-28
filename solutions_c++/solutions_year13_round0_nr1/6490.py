#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
#include<string.h>
char *board;
int evaldot(int w,int x,int y,int z)
{
	if(board[x]=='.'||board[y]=='.'||board[z]=='.'||board[w]=='.')
	return 0;
	return 3;
}
int eval(int x,int y,int z,int w,char val)
{
	if(board[x]==val&&board[y]==val&&board[z]==val&&board[w]==val)
	return 0;
	else if(board[x]=='T'&&board[y]==val&&board[z]==val&&board[w]==val)
	return 0;
	else if(board[x]==val&&board[y]=='T'&&board[z]==val&&board[w]==val)
	return 0;
	else if(board[x]==val&&board[y]==val&&board[z]=='T'&&board[w]==val)
	return 0;
	else if(board[x]==val&&board[y]==val&&board[z]==val&&board[w]=='T')
	return 0;
	return 1;
}

int chkwin(int x,char val)
{
	if(eval(x+0,x+1,x+2,x+3,val)==0)
	return 1000;
	if(eval(x+8,x+5,x+6,x+7,val)==0)
	return 1000;
	if(eval(x+12,x+13,x+10,x+11,val)==0)
	return 1000;
	if(eval(x+15,x+16,x+17,x+18,val)==0)
	return 1000;
	if(eval(x+0,x+5,x+10,x+15,val)==0)
	return 1000;
	if(eval(x+1,x+6,x+11,x+16,val)==0)
	return 1000;
	if(eval(x+2,x+7,x+12,x+17,val)==0)
	return 1000;
	if(eval(x+3,x+8,x+13,x+18,val)==0)
	return 1000;
	if(eval(x+0,x+6,x+12,x+18,val)==0)
	return 1000;
	if(eval(x+3,x+7,x+11,x+15,val)==0)
	return 1000;

	if(evaldot(x+0,x+1,x+2,x+3)==0)
	return 100;
	if(evaldot(x+8,x+5,x+6,x+7)==0)
	return 100;
	if(evaldot(x+12,x+13,x+10,x+11)==0)
	return 100;
	if(evaldot(x+15,x+16,x+17,x+18)==0)
	return 100;
	if(evaldot(x+0,x+5,x+10,x+15)==0)
	return 100;
	if(evaldot(x+1,x+6,x+11,x+16)==0)
	return 100;
	if(evaldot(x+2,x+7,x+12,x+17)==0)
	return 100;
	if(evaldot(x+3,x+8,x+13,x+18)==0)
	return 100;
	if(evaldot(x+0,x+6,x+12,x+18)==0)
	return 100;
	if(evaldot(x+3,x+7,x+11,x+15)==0)
	return 100;

	return 10;

}
void main()
{
int e=0,n1,n2,i,len,num;
fstream fl,fl2;
clrscr();
ifstream file( "input.in", ios::binary | ios::ate);
len=file.tellg();
file.close();
board=new char[len];
fl.open("input.in",ios::in|ios::out);
fl2.open("ouput.ou",ios::in|ios::out);
int c = fl.peek();
fl>>num;
c = fl.peek();
for(i=0;c!=EOF;i++)
	{
	fl.get(board[i]);
	c = fl.peek();
}
for(i=0;i<num;i++)
{
	e=e+21;
	if(i==0)
	e=1;
	fl2<<"Case #";
	fl2<<i+1;
	fl2<<": ";
	n1=chkwin(e,'X');
	if(n1==1000)
	fl2<<"X won";
	else
	{
		n2=chkwin(e,'O');
		if(n2==1000)
		fl2<<"O won";
		else if(n2==10)
		fl2<<"Draw";
		else
		fl2<<"Game has not completed";
	}
	fl2<<"\n";
}
//getch();
}
