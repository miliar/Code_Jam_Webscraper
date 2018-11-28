#include <iostream>
#include <math.h>
using namespace std;
#include <fstream>
using std::ifstream;
using std::ofstream;

int main()
{
	ifstream indata;
	indata.open("A-large.in");
	ofstream outdata;
	outdata.open("A-large.out");
	int t;
	indata>>t;
	for(int i=1; i<=t; i++)
	{
		int n;
		indata>>n;
		unsigned long int m[n], y=0, z = 0, w = 0;
		for(int j=0; j<n; j++)
		{
			indata>>m[j];
			if(j>0 && m[j]<m[j-1])
			{
				y = y + m[j-1] - m[j];
				if((m[j-1] - m[j]) > w)
					w = m[j-1] - m[j];
			}
		}
		for(int j=0; j<(n-1); j++)
		{
			if(m[j]<=w)
				z = z + m[j];
			else
				z = z + w;
		}
		outdata<<"Case #"<<i<<": "<<y<<" "<<z<<"\n";
	}
	indata.close();
	outdata.close(); 
}
