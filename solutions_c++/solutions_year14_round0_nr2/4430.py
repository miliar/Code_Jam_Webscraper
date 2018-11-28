#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <cstdio>

using namespace std;
int main() {
	int t,ff;
	long double c,f,x,s,ns,rg,tt,ntt,res;
	freopen ("B-large.in", "r", stdin);
	freopen ("b.out", "w", stdout);
	
	cin >> t;
	for (int h=1;h<t+1;h++) {
		cin >> c >> f >> x;
		//else {
			s=2;
			//rg=x;
			tt=x/s;
			res=0;
			ff=0;
			while (ff==0) {
				//tt=x/s;
				//cout << 1 << endl;
				if (c>=x) {res+=x/s;ff=1;}
				else {
					ns=s+f;
					ntt=c/s+x/ns;
					if (ntt<tt) {
						res+=c/s;
						s=ns;
						tt=x/s;	
					}
					else {
						ff=1;
						res+=x/s;
					}
				}

			}
			std::cout.precision(10);
			std::cout << "Case #" << h << ": " << res << endl;
	
	}
	
	fclose(stdout);
	return 0;
}