#include<fstream.h>
#include<conio.h>
#include<stdlib.h>
void main()
{
clrscr();
ifstream d("input1.txt");
char test[100];
d>>test;
int z=atoi(test),S[4][4];
for(int i=1;i<=z;i++)
	{
	d>>test;
	int d1=atoi(test);
	for(int y=0;y<4;y++)
		for(int x=0;x<4;x++)
		   {	d>>test;
			S[y][x]=atoi(test);}
	d>>test; int S1[4][4];
	int d3=atoi(test);
	for(y=0;y<4;y++)
		for(x=0;x<4;x++)
		       {	d>>test;
			 S1[y][x]=atoi(test); }
	int iop=0,crd=0;
	for(x=0;x<4;x++)
		for(y=0;y<4;y++)
			{
		    if(S[d1-1][x]==S1[d3-1][y])
		      {	iop++;
			crd=S[d1-1][x]; }}

	ofstream po("output.txt", ios::app);

	if(iop==1)
		po<<"Case #"<<i<<": "<<crd<<endl;
	else if(iop>1)
		po<<"Case #"<<i<<": Bad magician!"<<endl;
	else
		po<<"Case #"<<i<<": Volunteer cheated!"<<endl;

	po.close();
	}

  d.close();
}