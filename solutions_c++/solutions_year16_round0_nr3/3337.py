#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;
string to_bin(int val) {
	string res = "";
	while (val) {
		if (val%2) {
			res = "1" + res;
		} else {
			res = "0" + res;
		}
		val/=2;
	}
	return res;
}
long get_rem_base(const string& coin, int base) {
	unsigned long long pow = 1;
	unsigned long long res = 0;
	for (int i = coin.length()-1; i>=0; --i) {
		if (coin[i] == '1') {
			res += pow;
		}
		pow *= base;
	}
	// cout << res << endl;
	unsigned long long  stop = std::pow(res, 0.5) + 2;
	for (unsigned long long i = 2; i < stop; ++i) {
		if(res%i == 0) {
			return i; // Return the number that evenly divides it
		}
	}
	return -1;
}
int main() {
	fstream fin;
	fin.open("input.txt");
	int cases = 0;
	fin >> cases;
	for (int rnd = 0; rnd < cases; ++rnd) {
		// Do each case here
		int N, J;
		fin >> N >> J;
		long min_val = 1;
		min_val += pow(2.0, N-1);
		// cout << min_val<< endl;
		int solved = 0;
		cout << "Case #" << rnd+1 << ":" << endl;
		while (solved < J) {
			string coin = to_bin(min_val);
			// cout << "Coin: " << coin << endl;
			long divisors[9];
			bool good = true;
			for (int i = 2; i < 11; ++i) {
				divisors[i-2] = get_rem_base(coin, i);
				if (divisors[i-2] == -1) {
					good = false;
					break;
				}
			}
			if (good) {
				cout << coin;
				for (int i = 0; i < 9; ++i) {
					cout << " " << divisors[i];
				}
				cout << endl;
				solved++;
			}
			min_val+=2;
		}
		
		// 
	}
	fin.close();
	return 0;
}