#include <cstdlib>
#include <fstream>
#include <iomanip>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("out.txt");

int main() {
	int t;
	double c,f,x,speed,curtime;
	fin>>t;
	for (int test=0;test<t;test++) {
		fin>>c>>f>>x;
		if(x<c) fout<<fixed<<setprecision(10)<<"Case #"<<test+1<<": "<<x/2.0<<endl; else {
			curtime=0;
			speed=2.0;
			while(1) {
				if(x/speed>c/speed+x/(speed+f)) {
					curtime+=c/speed;
					speed+=f;
				} else break;
			}
			fout<<fixed<<setprecision(10)<<"Case #"<<test+1<<": "<<curtime+x/speed<<endl;
		}
	}
	return 0;
}