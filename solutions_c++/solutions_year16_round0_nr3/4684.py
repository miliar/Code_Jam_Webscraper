#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

int isDivisible(unsigned long long x) {
	if (x == 1 || x == 2) return 0;
	for (int i = 2; i < sqrt(x) + 1; i++) {
		if ((x % i) == 0) {
			return i;
		}
	}
	return 0;
}

unsigned long long coinToBase(string& c, int base) {
	unsigned long long sum = 0;
	for (int i = 0; i < c.size(); i++) {
		sum += pow(base, i) * ((c.at(c.size() - i - 1) == '0') ? 0 : 1);
	}
	return sum;
}

string generateCoin(int x, int n) {
	stringstream s;
	s << '1';
	int i = 0;

	if (x != 0) {
	while (x > 0) {
		s << x % 2;
		x /= 2;
		i++;
	}
	}

	while (s.str().size() + 1 < n) {
		s << '0';
	}
	s << '1';
	string st = s.str();

	for (int i = 0; i < st.size() / 2; i++) {
		char c = st.at(i);
		st.at(i) = st.at(st.size() - 1 - i);
		st.at(st.size() - 1 - i) = c;
	}
	return st;
}

int main() {

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N, J;
		cin >> N >> J;

		int i = 0;
		cout << "Case #" << t + 1 << ":" << endl;
		while (J > 0) { //for each of the J jamcoins
			
			string jamcoin = generateCoin(i, N); //generate a coin and check it
			i++;
			if (jamcoin.size() > N) break;
			stringstream divisors;
			int base;
			for (base = 2; base <= 10; base++) { 
				int d = isDivisible(coinToBase(jamcoin, base));
				if (d != 0) {
					divisors << d;
					if (base != 10)
						divisors << " ";
				}
				else
					break;
			}
			if (base == 11) {
				cout << jamcoin << " " << divisors.str() << endl;
				J--;
			}
			
		}

	}



	return 0;
}