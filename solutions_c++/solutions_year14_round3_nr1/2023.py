/*Author: Vasile Mihail-Raul
Mail: vasile.raul@webmonsters.ro*/

#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>

using namespace std;

int main(int argc, char* argv[]) { 
	int N;
	scanf("%d", &N);
	for(int i = 1 ; i <= N ; i++) {
		int A, B;
		scanf("%d/%d", &A, &B);
		bool found = false;
		for(int j = 0 ; j < 10 ; j++) {
			if(B == pow(2, j)) 
				found = true;
		}
		if(found == false) {
			printf("Case #%d: impossible\n", i);
		} else {
			int sol = 0;
			while(B > A) {
				sol++;
				B /= 2;
			}
			printf("Case #%d: %d\n", i, sol);
		}
	}
	return 0;
}