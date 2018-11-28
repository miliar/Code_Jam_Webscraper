#include <iostream>
using namespace std;


void solve (int N){
	if (N == 0){
		cout << " INSOMNIA" << endl;
		return;
	}
	
	int * dig = new int [10];
	int sum = 0;
	
	int finished = 0;
	while (!finished){
		sum += N;
		int aux = sum;
		while (aux){
			dig[aux % 10] = 1;
			aux /= 10;
		}
		finished = 1;
		for (int i = 0; i < 10; i++)
			if (dig[i] == 0) finished = 0;
	}
	
	cout << " " << (sum) << endl;
}


int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ":";
		int N;
		cin >> N;
		solve(N);
	}
	return 0;
}
