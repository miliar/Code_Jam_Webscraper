#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int A, B, K;
		cin >> A >> B >> K;
		int total = 0;
		for(int i = 0; i < A; i++){
			for(int j = 0; j < B; j++){
				int s = (i&j);
				bool S = s < K;
				if (S) total++;
				}
			}
		cout << "Case #"<< t << ": " << total << endl;
	}
}
