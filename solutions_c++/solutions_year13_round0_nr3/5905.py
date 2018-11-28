#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int T,i,A,B,j,g,c[100],e,co(0);
	double nb;
	bool n(false);
	cin >> T;
	for(i = 0; i < T; i++) {
		cin >> A >> B;
		co = 0;
		for(j = A; j <= B; j++) {
			n = false;
			if(j > 9) {
				e = (int)log10(j)+1;
				for(g = 0; g < e; g++) {
					c[g] = j/pow(10.0, (double)e-(g+1));
					if(g > 0) c[g]%=10;
				}
				for(g = 0; g < e/2; g++) {
					if(c[g] != c[(e-1)-g]) {
						n = true;
						break;
					}
				}
			}
			if(!n) {
				nb = sqrt(j);
				if(nb - (int)nb > 0) {
					n = true;
				} else if((int)nb > 9) {
					e = (int)log10((int)nb)+1;
					for(g = 0; g < e; g++) {
						c[g] = (int)nb/pow(10.0, (double)e-(g+1));
						if(g > 0) c[g]%=10;
					}
					for(g = 0; g < e/2; g++) {
						if(c[g] != c[(e-1)-g]) {
							n = true;
							break;
						}
					}
				}
			}
			if(!n) co++;
		}
		cout << "Case #" << i+1 << ": " << co << endl;
	}
	return 0;
}