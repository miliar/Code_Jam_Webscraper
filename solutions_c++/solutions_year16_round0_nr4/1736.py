#include <algorithm>
#include <stdio.h>
#include <vector>
#include <set>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
	ifstream input;
	input.open("D-small-attempt1.in");
	freopen("out","w",stdout);
	long long int T, K, C, S;
	input>>T;

	for(int t=0; t<T; t++){
		printf("Case #%d: ",t+1);
		input>>K>>C>>S;
		long long int base, step;
		step = 0;
		base = 1;
		for(int c=0; c<C; c++){
			step+=base;
			base*=K;
		}

		for(long long int k=0; k<K; k++){
			printf("%lld ", k*step+1);
		}
		printf("\n");
	}
}