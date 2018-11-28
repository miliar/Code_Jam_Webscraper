#include <iostream>
#include <fstream>
#include <iostream>

using namespace std;


int main(void){
	ifstream in("A-small-attempt0.in") ;
	ofstream out("a.out") ;
	int t, n=1;
	
	in >> t ;
	while(n<=t){
		out << "Case #" << n << ": " ;
		long double r, q, s;
		int y=0;
		in >> r >> q;
		s=(r+1)*(r+1)-r*r;
		while(s<=q){
			y++;
			r+=2;
			s=s+(r+1)*(r+1)-r*r;
			}
		out  << y <<  endl ;
		n++;
		}
	return 0;
	}
