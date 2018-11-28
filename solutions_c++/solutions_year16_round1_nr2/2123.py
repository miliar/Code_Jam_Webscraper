#include <iostream> 
using namespace std;

void solve_case(int T){
	int N;
	int heights[2501] = {0};
	int tmp;
	cin >> N;

	for (int i = 0; i < 2 * N - 1; i++){
		for (int j = 0; j < N; j++){
			cin >> tmp;
			heights[tmp]++;
		}
	}

	cout << "Case #" << T << ": ";

	for (int i = 1; i <= 2500; i++){
		if (heights[i] % 2 == 1){
			cout << i << " ";
		}
	}

	cout << endl;
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  solve_case(i);
  	}
  	return 0;
}