#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){
	int T;
	cin >> T;

	for(int i=1; i<=T; i++){
		int K, C, S;
		cin >> K >> C >> S;

		printf("Case #%d:", i);
		for(int j=1; j<=K; j++){
			printf(" %d", j);
		}
		printf("\n");
	}

	return 0;
}
