#include <iostream>

using namespace std;
int A, B, K;

int calculate_ways(){	
	int ways = 0;
	for(int i = 0; i < A; ++i){
		for(int j = 0; j < B; ++j){
			int res = i&j;
			if(res < K){
				ways++;
			}
		}
	}
	return ways;
}

int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		cin >> A;
		cin >> B;
		cin >> K;
		cout << "Case #" << i << ": " << calculate_ways() << endl;
	}
	return 0;
}

