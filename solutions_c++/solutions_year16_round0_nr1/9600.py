#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]){
	long long int  number, number_digits, divisor, digit, copy, last_number, n;

	freopen("Code Jam Classification - (A).txt", "w", stdout);

	cin >> n;

	for (long long int counter = 1; counter <= n; counter++){

		set <long long int> digits;
		bool sleep = false;

		cin >> number;

		if (number == 0){ 
			if (number == 0) printf("Case #%lld: INSOMNIA\n", counter);
			continue;
		}
		for (long long int j = 1; j <= 1000000; j++){
			copy = number*j;
			number_digits = log10((float)copy) + 1;

			for (int i = number_digits - 1; i >= 0; i--) {
				divisor = pow((float)10, i);
				digit = copy / divisor;
				copy -= digit * divisor;

				digits.insert(digit);
			}

			last_number = number*j;
			if (digits.size() == 10){
				sleep = true;
				break;
			}
		}

		if(sleep) printf("Case #%lld: %lld\n", counter, last_number);
		else printf("Case #%lld: INSOMNIA\n", counter);
	}

	fclose(stdout);

	return 0;
}