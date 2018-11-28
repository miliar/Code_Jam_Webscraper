#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main () {
	int T,S,res,acc;
	char shyness_array[1010];
	scanf("%d",&T);
	for ( int w = 1; w <= T; w++ ) {
		scanf("%d %s",&S,shyness_array);
		res = 0;
		acc = 0;
		for (int i = 0; i <= S; i++) {
			if ( (shyness_array[i] - '0') != 0 && acc < i ) {
				res += (i - acc);
				acc += (i - acc);
			}
			acc += (shyness_array[i] - '0');
		}
		printf("Case #%d: %d\n",w,res);
	}
	return 0;
}
