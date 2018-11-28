#include<fstream>
#include<iostream>

using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B.out");
	int t;
	fin>>t;
	for(int cas=1;cas<=t;++cas)
	{
		fout.precision(30);
		fout<<"Case #"<<cas<<": ";
		double c,f,x;
		fin>>c>>f>>x;
		double timesofar=0;
		double rate=2;
		double timetilnext=c/rate;
		double timetilfinish=(x-c)/rate;
		while(timetilfinish>x/(rate+f))
		{
			rate+=f;
			timesofar+=timetilnext;
			timetilnext=c/rate;
			timetilfinish=(x-c)/rate;
		}
		fout<<timesofar+x/rate<<'\n';
	}
	return 0;
}
