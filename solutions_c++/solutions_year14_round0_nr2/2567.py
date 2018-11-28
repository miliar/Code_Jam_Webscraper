#include"../std_lib_facilities.h"

int main()
{
	ifstream ifs("input.in");
	ofstream ofs("output.out");
	int solve,count=0;
	ifs>>solve;
	while (solve>count)
	{
		++count;
		double c,f,x;
		ifs>>c>>f>>x;
		double min=x;
		double p=2;
		double build=0;
		double s=x/p;
		while (s<min)
		{
			min=s;
			build+=c/p;
			p+=f;
			s=build+x/p;
		}
		ofs<<"Case #"<<count<<": "<<setprecision(7)<<setiosflags(ios::fixed)<<min<<endl;
	}
	ifs.close(); ofs.close();
	return 0;
}