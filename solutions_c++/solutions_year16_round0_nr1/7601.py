#include <iostream>
using namespace std;

int main() {
	int T, N;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> N;
		if(N == 0) cout << "Case #" << i+1 << ":INSOMNIA" << endl;
		else {
			int k = 1, num; bool done = false;
			int arr[10] = {0};
			while(1) {
				num = k * N;
				while(num) {
					arr[num%10] = 1;
					num = num/10;
				}
				int j = 0;
				for(; j < 10; j++) {
					if(arr[j] == 1) continue;
					else break;
				}
				if(j == 10) break;
				k = k+1;
			}
			cout << "Case #" << i+1 << ":" << k*N << endl;
		}
	}
return 0;
}
