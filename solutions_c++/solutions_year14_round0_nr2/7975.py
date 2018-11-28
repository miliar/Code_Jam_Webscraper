#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;



int main() {
	int round, num, cnt, i, j, k, res;
	double temp1, temp2, temp3, temp4;
	double c, f, x;
	double post, pret, spe;
	double ee = 1e-10;
	
	cin>>round;
	for (i = 1; i <= round; i++) {
		cin>>c>>f>>x;
		post = x / 2;
		pret = 0;
		spe = 2;
		
		for (;;) {
			temp1 = c / spe + x / (spe + f);
			if (temp1 > post) {
				break;
			}
			pret = pret + c / spe;
			post = x / (spe + f);
			spe = spe + f;
		}
		
		
		
		printf("Case #%d: %.7f\n", i, (pret + post));
	}
	
	return 0;
}

