#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		long double c,x,f, t=0, p=2;
		fin>>c>>f>>x;
		while (x/p > x/(p+f) + c/p) { 
			t+=c/p; p+=f;
		}
		fout<<"Case #"<<I+1<<": "<<fixed<<setprecision(10)<<t+x/p<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

