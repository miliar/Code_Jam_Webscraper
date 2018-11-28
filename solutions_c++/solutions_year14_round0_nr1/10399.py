#include<iostream>
using namespace std;
#include<conio.h>
#include<fstream>
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt2.in");
	fout.open("output.txt");
	int t,row1,row2,count,a[4][4],b[4][4],num;
	fin>>t;
	int k=0;
	while(k<t)
	{
		count=0;
		fin>>row1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				fin>>a[i][j];
		}
		fin>>row2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				fin>>b[i][j];
		}
		for(int i=0;i<4;i++)
				{	
				for(int j=0;j<4;j++)
					if(a[row1-1][i]==b[row2-1][j])
					{
						count++;
						num=a[row1-1][i];
					}
				}
	fout<<"Case #"<<k+1<<": ";
	if(count==0)
	fout<<"Volunteer Cheated!"<<endl;
	else if(count>1)
	fout<<"Bad Magician!"<<endl;
	else
	fout<<num<<endl;	
	++k;
	}
}