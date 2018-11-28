#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int countSeen(int n, int& cs, std::vector<int>& seen){
	while(n > 0){
		int d = n % 10;

		if(!seen[d]){
			seen[d] = 1;
			++cs;
		}
		n /= 10;
	}

	return cs;
}

int main(){
	int c, n, N;
	cin >> c;
	for(int i = 1; i <= c; ++i){
		cin >> N;
		n = N;

		if(!n){
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}

		const int D = 10;
		std::vector<int> seen(D);
		int cs = 0;

		while(countSeen(n, cs, seen) < D){
			n += N;
		}

		cout << "Case #" << i << ": " << n << endl;
	}
	return 0;
}
