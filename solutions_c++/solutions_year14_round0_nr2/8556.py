#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
using namespace std;

int main()
{
	int T;

	fstream inf("B-large.in",ios::in);
	fstream outf("outA.txt",ios::out);

	inf>>T;

	int k=0;
	while(k<T)
	{
		double c;
		double j=2;
		double f;
		double x;
		double sum=0;

		inf>>c>>f>>x;

		while(((c/j)+(x/(j+f)))<x/j)
		{
			sum+=c/j;
			j=j+f;
		}
		
		
		sum+=(x/j);
		setprecision(8);
		outf<<"Case #"<<k+1<<": ";
		outf<<fixed<<sum<<endl;
		k++;
	}
	return 0;
}
