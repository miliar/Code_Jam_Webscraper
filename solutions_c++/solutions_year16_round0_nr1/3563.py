#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		long long int n;
		cin >> n;
		long long int answer = 1;
		int dig[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int dec = 0;
		if (n == 0) answer = -1;
		else {
			//убираем все 0
			while (n > 10 && n % 10 == 0) {
				n /= 10;
				dec++;
			}
			if (dec > 0) dig[0] = 1;
			while (true) {
				int j;
				for (j = 0; j < 10; j++) {
					if (dig[j] == 0) break;
				}
				if (j >= 10) break;
				
				long long int nn = n * answer;
				while (nn > 0) {
					dig[nn % 10] = 1;
					nn /= 10;
				}
				answer++;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (answer == -1) cout << "INSOMNIA";
		else cout << n * (answer - 1);
		//возвращаем все 0
		for (int j = 0; j < dec; j++) {
			cout << 0;
		}
		cout << endl;
	}
	
	return 0;
} 
