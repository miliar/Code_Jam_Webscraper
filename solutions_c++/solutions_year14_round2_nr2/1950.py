#include <iostream>
using namespace std;

int main() {
	int A, B, K;
	int i, j;
	int T, t;
	int res;
	int flag;	

	cin >> T;
	for(t = 1; t <= T; t++) {
		res = 0;
		cin >> A >> B >> K;
		for(i = 0; i < A; i++)
		for(j = 0; j < B; j++) {
			flag = i & j;
//			cout <<  << " " << B << " " << flag << "\n";
			if(flag < K)
				res++;
		}
		cout << "Case #" << t << ": " << res << "\n";
	}

	return 0;
}
