#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <list>
#include <vector>

using namespace std;

double mysolve(ifstream &fi) {
	double c,f,x;
	fi>>c>>f>>x;
	double t0=x/2, t1=t0;
	for (int i=1;t1<=t0;++i)  {
		t0=t1;
		t1=x/(2+i*f)+t0-(x-c)/(2+(i-1)*f);
	}
	return t0;
}

int main()  {
	int n(0);
	double res(0);

	//ifstream fi("test.txt");
	//ifstream fi("C-large-1.in");
	ifstream fi("B-large.in");
	//ifstream fi("B-small-attempt0.in");
	ofstream fo("output.txt");
	fi>>n;
	for (int i(0);i<n;++i)  {
		res=mysolve(fi);
		//cout<<"Case #"<<i+1<<": "<<res<<endl;
		fo.precision(15);
		fo  <<"Case #"<<i+1<<": "<<res<<endl;
	}
	//cin>>n;
	return 0;
}