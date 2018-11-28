#include <iostream>
#include <fstream>
using namespace std;

int main(void)
{
	ifstream fin;
	fin.open("A-small-attempt2.in");
	ofstream fout;
	fout.open("A-small-attempt2.out");
	int t;
	fin>>t;
	int a,b,ae,be;
	int m[4][4],n[4][4];
	char *p;
	for(int i=0;i<t;i++)
	{
		//cin
		fin>>a;
		for(int j=0;j<4;j++) 
		for(int k=0;k<4;k++)
			fin>>m[j][k];
		
		fin>>b;
		for(int j=0;j<4;j++) 
		for(int k=0;k<4;k++)
			fin>>n[j][k];
		
		int c=0;
		int r=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
		    {
			 if(m[a-1][j]==n[b-1][k]) {r=m[a-1][j];c++;}
			}
		}
		
		fout<<"Case #"<<i+1<<": ";
		if(c==1) fout<<r<<endl;
		else if(c==0) fout<<"Volunteer cheated!"<<endl;
		else fout<<"Bad magician!"<<endl;
	}
	return 0;
}