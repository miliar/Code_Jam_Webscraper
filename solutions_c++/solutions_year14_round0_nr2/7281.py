#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t;
	fin>>t;

	double c,f,x;
	long double time=0.0;
	bool less=false;
	double cook;
	long double min_time=0;
	for(int i=0;i<t;++i)
	{	
		time=0.0;
		cook=2.0;
		less=false;
		fin>>c>>f>>x;
		int n=0;
		min_time=0;
		while(n<1000)
		{
			if(x<=c)
			{
				time=x/cook;
				min_time=time;
				less=true;
				break;
			}
			if(time+(x/cook)<=(time+(c/cook)+(x/(cook+f))))
			{
				time+=x/cook;
				if(min_time<time)
					min_time=time;
				break;
			}
			time+=(c/cook);
			cook+=f;
		}
		fout<<"Case #"<<i+1<<": ";
		fout<< setprecision(10) <<min_time<<endl;

	}
	
	



	return 0;
}