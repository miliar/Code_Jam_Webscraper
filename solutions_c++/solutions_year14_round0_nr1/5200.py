#include<iostream>
#include <fstream>
using namespace std;

int main()
{
	int t;
	ifstream fin("as.in");
	ofstream fout("a_small.out");
	fin>>t;
	for(int e=0; e<t; e++)
	{
		int ans1, ans2, count=0, x;
		int a1[4][4], a2[4][4];
		fin>>ans1;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				fin>>a1[i][j];
			}
		}
		fin>>ans2;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				fin>>a2[i][j];
			}
		}
		
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(a1[ans1-1][i]==a2[ans2-1][j])
				{
					x=a1[ans1-1][i];
					count++;
				}
			}
		}
		
		if(count==1)
		{
			fout<<"Case #"<<e+1<<": "<<x<<endl;
		}
		else if(count==0)
		{
			fout<<"Case #"<<e+1<<": "<<"Volunteer cheated!"<<endl;
		}
		else
		{
			fout<<"Case #"<<e+1<<": "<<"Bad magician!"<<endl;
		}
		
	}
	fin.close();
	fout.close();	
	return 0;
}
