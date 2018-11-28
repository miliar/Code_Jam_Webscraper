#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
	int x,c,r;
	int cases;
	fin>>cases;
	int i=0;
	while(i<cases)
	{
		fin>>x;
		fin>>r;
		fin>>c;
		if((r*c)%x == 0 )
		{
			if((x-1<=c && x-1<=r))
			{
				fout<<"Case #"<<i+1<<":"<<" GABRIEL\n";
				
			}
			else
			{
			fout<<"Case #"<<i+1<<":"<<" RICHARD\n";
			}
		}
		else
		{
			fout<<"Case #"<<i+1<<":"<<" RICHARD\n";
		}
		i++;
	}
	system("pause");
	return 0;
}