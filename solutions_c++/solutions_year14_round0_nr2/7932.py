#include<iostream>
#include<fstream>
#include<iomanip>
using  namespace std;
#include <iostream>
using namespace std;

double c, f, s, x, cur;
int TC;

int main() {
    ifstream fl("B-large.in");
    ofstream ofl("aaa.txt");
	fl >> TC;
	for( int cas = 1; cas <= TC; cas++ ) {
		fl >> c >> f >> x;
		cur = 2;
		s = 0;
		while( x / cur > c / cur + x / (cur + f) ) {
			s += c / cur;
			cur += f;
		}
		s += x / cur;
		 ofl<<"Case #"<<cas<<": "<<setprecision(12)<<s<<"\n" ;
	}
	return 0;
}
