#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t,k;
	double c,f,x,y,r;
	fin>>t;
	for (k=1;k<=t;k++)
	{
		fin>>c>>f>>x;
		r=2;y=0;
		while (true)
		{
			if (x/r<c/r+x/(r+f))
			{
				y+=x/r;
				break;
			}
			y+=c/r;
			r+=f;
		}
		fout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<y<<endl;
	}
	return 0;
}