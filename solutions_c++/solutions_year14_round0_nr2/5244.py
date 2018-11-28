#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

int t, kol;
long double c, f, x;

int main()
{
	//ifstream cin("input.txt");
	//ofstream cout("output.txt");
	cin>>t;
	for(int kol=1;kol<=t;kol++)
	{
		cin>>c>>f>>x;
		int kk=0;
		long double time=0., p=2., ans=1000000000.;
		for(int i=0; i<=1000000; ++i)
		{
			ans=min(ans, time+x/p);
			time+=c/p;
			p+=f;
		}

		cout<<"Case #"<<kol<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}
	return 0;
}