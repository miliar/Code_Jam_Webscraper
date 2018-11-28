#include <iostream>
#include <fstream>
#include <string>
#include <process.h>
using namespace std;
int try1[101][5][5],try2[101][5][5],gues1[101],gues2[101]; 
void calout(int); // calculate logic and write to file

void calout(int i)
{	
	ofstream outf;
	outf.open("sampleoutput.txt", ios::app);
	int result; // 0, 1, >1
	int count=0;
	int no;
	for(int j=1;j<=4;j++)
	{	
		for(int k=1;k<=4;k++)
		{
			if(try1[i][gues1[i]][j]==try2[i][gues2[i]][k])
			{	
				no=try1[i][gues1[i]][j];
				count++;
			}
		}
	}
	switch(count)
	{
		case 0:
			outf<<"Case #"<<i<<": Volunteer cheated!"<<endl;
			break;
		case 1:
			outf<<"Case #"<<i<<": "<<no<<endl;
			break;
		default:
			outf<<"Case #"<<i<<": Bad magician!"<<endl;
	}
	outf.close();
}
int main()
{	
	int i,j,k;
	ifstream inf;
	inf.open("A-small-attempt0.in");
	if(!inf)
	{
		cerr << "error in opening file" << endl;
        exit(1);
	}
	string strInput;
	int cn;
	inf>>cn;
	for(i=1;i<=cn;i++)
	{
		inf>>gues1[i];
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				inf>>try1[i][j][k];
			}
		}	
		inf>>gues2[i];
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				inf>>try2[i][j][k];
			}
		}		
	}
	
	for(i=1;i<=cn;i++)
	{
		calout(i);		
	}
	
	inf.close();
	system("pause");		
}
