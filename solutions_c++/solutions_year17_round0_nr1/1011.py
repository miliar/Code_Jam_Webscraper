#include <iostream>
#include <string>
using namespace std;

int main(){
	int T, K, flips;
	bool impossible;
	string S;
	cin >> T;

	for (int t = 1; t <= T; ++t){
		cin >> S >> K;
		flips = 0;
		impossible = false;
		for (int i = S.length() - 1; i >= K - 1; --i){
			if (S[i] == '-'){
				for (int j = i; j > i - K; --j) S[j] = (S[j] == '-')? '+':'-';
				++flips;
			}
		}
		for (int i = K - 2; i >= 0; --i)
			if (S[i] == '-'){
				impossible = true;
				break;
			}

		if (impossible){
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}else{
			cout << "Case #" << t << ": " << flips << endl;
		}
	}

	return 0;
}