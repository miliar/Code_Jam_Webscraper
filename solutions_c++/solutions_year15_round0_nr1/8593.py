#include <iostream>
using namespace std;
int main(int argc, char const *argv[]){
	int T,S;
	int *s;
	char c;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		cin >> S;
		s = new int[S + 1];
		for(int k = 0; k <= S; ++k){
			cin >> c;
			s[k] = c - '0';
		}

		int sum = s[0], guests = 0;
		for(int k = 1; k <= S; ++k){
			if(sum < k){
				guests += (k - sum);
				sum = k;
			}
			sum += s[k];
		}
		cout << "Case #" << t << ": " << guests << endl;
		delete[] s;
	}
	return 0;
}