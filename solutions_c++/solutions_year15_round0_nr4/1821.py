#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
fstream fin,fout;
int main()
{
	fin.open("in.cpp");
	fout.open("output.cpp");
	int t,x,r,c;
	fin>>t;
	for(int i=1;i<=t;i++)
	{
		
		fin>>x>>r>>c;
		int mn=min(r,c);
		int mul=r*c;
		fout<<"Case #"<<i<<": ";
		if(mul%x!=0||(x>=2*mn-1&&x>mn+1))
		{
			fout<<"RICHARD\n";
		}
		else fout<<"GABRIEL\n";
	}
	fin.close();
	fout.close();
}
