#include <iostream>
using namespace std;

void print_sol(int K, int C){
	int times = (K + C - 1) / C;
	for (int i = 0; i < times; i++){
		long val = 0;
		for (int j = 0; j < C; j++)
			val = val * K + (i * C + j) % K;
		cout << " " << val + 1;
	}
	cout << '\n';
}

int main(){
	int times, K, C, S;
	cin >> times;

	for (int i = 1; i <= times; i++){
		cin >> K >> C >> S;
		cout << "Case #" << i << ":";
		if ( S * C < K )
			cout << " IMPOSSIBLE\n";
		else
			print_sol(K, C);
	}
	return 0;
}
