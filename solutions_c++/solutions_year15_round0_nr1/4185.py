
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
	in.open("A-large.in");
	ofstream out;
	out.open("A-large.out");
	int t;
	in>>t;
	for(int i=1; i<=t; i++)
	{
		int  m;
		in>>m;
		int v[m+1];
		string s;
		in>>s;
		for(int j=0; j<=m; j++)
		{
			v[j] = (int)(s[j]) - 48;
			//out<<v[j];
		}
		//out<<"\n";

		int o=0, count=v[0];
		for(int j=1; j<=m; j++)
		{
			if((count<j) && (v[j]>0))
			{
				o += (j - count);
				count += (j - count);
			}

			count += v[j];
		}
		out<<"Case #"<<i<<": "<<o<<"\n";

	}
	in.close();
	out.close(); 

}
