#include <iostream>
#include <fstream>

using namespace std;

int cnt = 0;

bool used[10];

void check(long long n) {
	 while(n > 0) {
	 	int dig = n % 10;
	 	if(!used[dig]) {
	 		cnt++;
            used[dig] = true;
        }
        n /= 10;
     }
}

int main() {

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	long long N;
	long long sum;

	for(int i = 0; i < T; i++) {
		cnt = 0;

		for(int i = 0; i < 10; i++) {
			used[i] = false;
		}
				
		cin >> N;

		if (N == 0) {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}

		sum = N;
		check(sum);
		while(cnt < 10) {
			sum += N;
			check(sum);
		}
		cout << "Case #" << i + 1 << ": " << sum << endl;
	}
	return 0;
}