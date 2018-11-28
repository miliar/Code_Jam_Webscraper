#include <iostream>
#include <math.h>
#include <string>

using namespace std;
#include <fstream>
using std::ifstream;
using std::ofstream;



int main()
{

	ifstream in;
	in.open("D-small-attempt0.in");
	ofstream out;
	out.open("D-small-attempt0.out");
	int t;
	in>>t;
	for(int i=1; i<=t; i++)
	{
		int x, r, c;
		in>>x>>r>>c;
		int p = r*c;
		if(p%x==0)
		{
			if((r>=x && c>=(x-1)) || (c>=x && r>=(x-1)))
				out<<"Case #"<<i<<": GABRIEL\n";
			else
				out<<"Case #"<<i<<": RICHARD\n";
		}
		else
			out<<"Case #"<<i<<": RICHARD\n";

	}
	in.close();
	out.close(); 

}
