#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <iterator>
using namespace std;

uint64_t ipow(int n, int p) {
	uint64_t num = 1;
	for(int i = 0; i < p; i++)
		num *= n;
	return num;
}
bool isPrime(uint64_t n) {
	if(n <= 1) {
		return false;
	} else if(n <= 3) {
		return true;
	} else if(n % 2 == 0) {
		return false;
	} else {
		int max = int(sqrt(double(n)) + 2);
		if(max > n)
			max = n-1;
		for(int i = 3; i <= max; i += 2) {
			if(n % i == 0) {
				return false;
			}
		}
	}
	return true;
}
uint64_t nonTrivialDivisor(uint64_t n) {
	//cout << "testing " << n << endl;
	if(n < 4) {
		return 1;
	} else {
		int max = int(sqrt(double(n)) + 3);
		if(max > n)
			max = (n/2) + 1;
		for(int i = max; i >= 2; i--) {
			if(n % i == 0) {
				//cout << n << " % " << i << endl;
				return i;
			}
		}
	}
	return 1;
}
uint64_t nonTrivDiv(uint64_t n) {
	if(n % 2 == 0)
		return 2;
	uint64_t max = uint64_t(sqrt(double(n)) + 3);
	if(max > n)
		max = (n/2) + 1;
	for(int i = 3; i <= max; i+= 2) {
		if(n % i == 0)
			return n;
	}
}
class Jamcoin {
  private:
	vector<bool> bits;
  public:
	uint64_t interpret(int base) {
		uint64_t res = 0;
		int i = 0;
		int l = bits.size();
		for(int j = 0; j < l; j++) {
			if(bits[l-1-j])
				res += ipow(base, i);
			i++;
		}
		return res;
	}
	bool validate(void) {
		if(bits.front() && bits.back()) {
			for(int i = 2; i <= 10; i++) {
				if(isPrime(interpret(i)))
					return false;
			}
			return true;
		}
		return false;
	}
	char* binaryStr(void) {
		int l = bits.size();
		char* binstr = new char[l+1];
		for(int i = 0; i < l; i++) {
			binstr[i] = (bits[i] ? '1' : '0');
		}
		binstr[l] = '\0';
		return binstr;
	}
	void printJamcoin(void) {
		cout << binaryStr();
		for(int i = 2; i <= 10; i++) {
			cout << ' ' << nonTrivialDivisor(interpret(i));
			//cout << ' ' << interpret(i);
		}
		cout << endl;
	}
	Jamcoin(string s) {
		int l = s.length();
		for(int i = 0; i < l; i++) {
			if(s[i] == '1')
				bits.push_back(true);
			else if(s[i] == '0')
				bits.push_back(false);
		}
	}
	Jamcoin(int n) {
		int tmp = n;
		while(tmp > 0) {
			bits.insert(bits.begin(), 1, (tmp & 1));
			tmp >>= 1;
		}
	}
};

class JamcoinGenerator {
  public:
	JamcoinGenerator(int n, int j) {
		int max = ipow(2, n) - 1;
		int count = 0;
		for(int i = ipow(2, n-1) + 1;count < j && i <= max; i++) {
			Jamcoin jc(i);
			if(jc.validate()) {
				jc.printJamcoin();
				count++;
			}
		}
	}
};

int main(void) {
	uint64_t uint = 0;
	int N, n, j;
	cin >> N;
	for(int i = 0; i < N; i++) {
		cin >> n >> j;
		cout << "Case #" << i+1 << ":\n";
		JamcoinGenerator jg(n, j);
	}
	return 0;
}
