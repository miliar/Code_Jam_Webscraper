#include<iostream>
#include<iomanip>
#include<fstream>

using namespace std;

int main()
{
	int t;
	ifstream fin("bl.in");
	ofstream fout("b_large.out");
	fin>>t;
	
	for(int e=1; e<=t; e++)
	{
		double c, f, x, sum=0.0, r=2.0;
		fin>>c>>f>>x;
		
		while((x/r)>((c/r)+(x/(r+f))))
		{
			sum+=c/r;
			r+=f;
		}
		
		sum+=x/r;
		
		fout<<"Case #"<<e<<": "<<fixed<<setprecision(7)<<sum<<endl;
	}
	
	return 0;
}
		
