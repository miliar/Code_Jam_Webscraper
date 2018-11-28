#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

bool checkIsPrime(long long n, long long &divisor) {

    divisor = 2;
	while (divisor * divisor < n) {
		divisor++;
		if (n % divisor == 0) return false;
	}

	return true;
}

void findJamcoin(int n, int k) {
	long long max_num = pow(2, n);
	vector<long long> divisors  (9, 0);
    
    for (long long i = 3; i < max_num && k > 0; ++i) {
	    
		bitset<16> num_test (i);
		string str_num = num_test.to_string();
		bool isValid = false;
		
		// if (str_num[0] == '0' || str_num[5] == '0') continue;
		if (str_num[0] == '0' || str_num[15] == '0') continue;	

		// Check base 2 first
		if (!checkIsPrime(i, divisors[0])) {
			
			// Check other bases
			isValid = true;
			for (int base = 3; base <= 10; ++base) {
				long long test_num = stol(str_num, 0, base);
				if (checkIsPrime(test_num, divisors[base-2])){
					isValid = false;
					break;
				}
			}
			
		}
		

		if (isValid) {
			// cout << i << endl;
			cout << str_num << " ";
			for (int idx = 0; idx < 9; ++idx) {
				cout << divisors[idx] << " ";
			}
			cout << endl;

			// cout << str_num << " ";
			// for (int base = 2; base <= 10; ++base) {
			// 	cout << stol(str_num, 0, base) << " ";
			// }
			// cout << endl;

			k--;
		}

	}

}

int main(int argc, char const *argv[])
{
	int num_test, t, n, k;
	cin >> num_test;

	for (int t = 1; t <= num_test; ++t)
	{
		cin >> n >> k;
		cout << "Case #" << t << ":" << endl;
		findJamcoin(n, k);
	}
	
	return 0;
	
}