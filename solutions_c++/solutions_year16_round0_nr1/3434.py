#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		unsigned long long n, n_copy;
		int  digits[10] = { 0 }, count = 0;
		cin >> n;
		if (n == 0) cout << "Case #"<<i<<": "<<"INSOMNIA" << endl;
		else{
			unsigned long long j = 1;
			n_copy = n;
			while (count != 10){
				n_copy = n*j;
				unsigned long long n_copy_copy = n_copy;
				while (n_copy_copy > 0){
					if (digits[n_copy_copy % 10] == 0){
						digits[n_copy_copy % 10]++;
						count++;
					}
					n_copy_copy /= 10;
				}
				j++;
			}
			cout << "Case #" << i << ": " << n_copy << endl;
		}
	}
	return 0;
}

