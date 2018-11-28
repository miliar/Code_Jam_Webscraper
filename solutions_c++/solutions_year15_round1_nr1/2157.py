#include <iostream>
#include <inttypes.h>
using namespace std;
int min(int a, int b){ 
	if (a < b) return a;
	return b;
}
int max(int a, int b){
	if (a > b) return a;
	return b;
}
void main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int N;
		cin >> N;
		int * M = new int[N];
		int64_t y = 0, z = 0;
		int maxE = 0, last = 10001;
		cin >> M[0];
		last = M[0];
		for (int m = 1; m < N; m++){
			cin>>M[m];
			int diff = M[m-1]-M[m];
			maxE = max(maxE, diff);
			if (diff > 0)y += diff;
		}
		//cout << "MaxE " << maxE << endl;
		for (int m = 1; m < N; m++){
			z += min(M[m-1], maxE);
		}
		cout << "Case #" << t << ": " << y << " " << z << endl;
	}

}