#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int n = 0; n < T; n++){
		int D;
		cin >> D;
		vector<int> P(D,0);
		for (int i = 0; i < D; i++){
			cin >> P[i];
		}
		vector<int> minnn(1000,100000);
		for(int k = 1; k < 1000; k++){
			int flips = 0;
			for(auto x : P){
				flips += (x-1) / k;
			}
			minnn[k] = flips + k;
		}

		int temp = *(min_element(minnn.begin(), minnn.end()));
		cout << "Case #" << n+1 << ": " << 	temp << endl;
	}
}