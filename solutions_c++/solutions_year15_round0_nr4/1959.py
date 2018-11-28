#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int t,x,r,c;
	fstream fin,fout;
	
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);
	fin>>t;
	for(int i=1;i<=t;i++)
	{
		fin>>x>>r>>c;
		if(x==1)
		{
			fout<<"Case #"<<i<<": "<<"GABRIEL\n";
		}
		else
		{
			if((r%x==0&&c>=(x-1))||(c%x==0&&r>=(x-1)))
			{
				fout<<"Case #"<<i<<": "<<"GABRIEL\n";
			}
			else
			{
				fout<<"Case #"<<i<<": "<<"RICHARD\n";
			}
		}

	}
}