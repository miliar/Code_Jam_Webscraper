#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

unsigned long long mycase(ifstream &fi, ofstream &fo)  {
	unsigned long long r,t,res(0);
	fi>>r>>t;
	long double x(0),b=r,c=t;
	b=b+b-1;
	;
	x=(-b+sqrt(b*b+8*c))/4.0;
	res=floor(x);
	return res;
}

int main()  {
	int n(0);
	int i(0);
	ifstream fi("A-small-attempt0.in");
	fi>>n;
	ofstream fo("output.txt");
	for (i=0;i<n;++i)
		fo<<"Case #"<<i+1<<": "<<mycase(fi,fo)<<endl;
	cout<<"End program"<<endl;
	//cin>>n;
	return 0;
}
