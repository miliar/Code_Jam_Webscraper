#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++){
		long long n;
		cin >> n;
		if (n == 0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		int digits[10] = {0};
		long long k = 1;
		while (1){
			long long  temp = k*n;
			while (temp != 0)
			{
				digits[temp % 10] = 1;
				temp /= 10;
			}
			int sum = 0;
			for (int j = 0; j < 10; j++){
				sum += digits[j];
			}

			if (sum == 10){
				cout << "Case #" << i+1 << ": " << k*n << endl;
				break;
			}
			k++;
		}
	}
	return 0;
}