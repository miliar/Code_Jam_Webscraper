#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;

int main()
{
	int x,y,g,a[16],b[16],c,d,t;
		
	ifstream fin("input.txt");
	ofstream fout("output.txt");
		
	fin>>t;
	
	for(int k=0;k<t;++k)
	{
		c=0;
		
		fin>>x;
		for(g=0;g<16;g++)
		fin>>a[g];
				
		fin>>y;
		for(g=0;g<16;++g)
		fin>>b[g];
		
		for(int i=(x-1)*4;i<x*4;i++)
		{
			for(int j=(y-1)*4;j<y*4;j++)
			{
				if(a[i]==b[j])
				{
					c++;
					d=a[i];	
				}
			}
		}
		fout<<"case#"<<k+1<<": ";
		if(c==0)
			fout<<"Volunteer cheated!";
		else if(c==1)
			fout<<d;
		else
			fout<<"Bad magician!";
		fout<<endl;
	}
	return 0;
}