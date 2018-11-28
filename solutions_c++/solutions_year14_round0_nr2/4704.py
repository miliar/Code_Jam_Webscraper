#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream f1("B-small-attempt0.in");
	ofstream f2("out.txt");
	int T;
	f1>>T;
	for(int tt=0;tt!=T;++tt)
	{
		f2<<"Case #"<<tt+1<<": ";
		double C,F,X;
		f1>>C>>F>>X;
		double a=F*X/C-F;
		int t=ceil((a-2)/F);
		double ans=0;
		double c=2;
		for(int i=0;i<t;++i)
		{
			ans+=C/c;
			c+=F;
		}
		ans+=X/c;
		f2.setf(ios::fixed, ios::floatfield);
		f2.precision(7);
		f2<<ans<<endl;
	}
	return 1;
}