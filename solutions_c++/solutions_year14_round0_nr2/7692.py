#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;
int main(int argc, char *argv[]) {
	int n;
	cin >> n;
	for (int y=0;y<n;y++) {
		long double c,f,x,o;
		cin >> c >> f >> x;
		long double p=0;
		o=0;
		long double pn=2;
		while (p==0) {
			if (o+(c/pn)+x/(pn+f)<o+x/pn) {
				o=o+c/pn;
				pn=pn+f;
			}
			else {
				p=1;
				o=o+x/pn;
				cout.setf(ios::fixed,ios::floatfield);
				cout.precision(10);
				cout << "Case #" << y+1 << ": " << o << endl;
			}
			
		}
	}
}