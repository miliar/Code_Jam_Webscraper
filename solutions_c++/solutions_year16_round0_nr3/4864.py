
#include <iostream>
#include <iomanip>

using namespace std;

void printJCoin(int jcoin, int n) {
  for(int i = 1; jcoin > 0; i++) {
    int bit = (jcoin >> (n - i)) & 1;
    jcoin &= ~(1 << (n - i));
    cout << bit;
  }
}

long convertJCoin(int jcoin, int n, int base) {
  unsigned long converted = 0;
  for(int i = 1; jcoin > 0; i++) {
    unsigned int bit = (jcoin >> (n - i)) & 1;
    jcoin &= ~(1 << (n - i));
    converted = converted * base + bit;
  }
  return converted;
}

int isPrime(long num) {
	int numBits = 0;
	for(long buf = num; buf > 0; numBits++, buf >>= 1);
	int maxVal = num >> (numBits / 2 - 1);
	for(int div = 3; div <= maxVal; div += 2) {
		if(num % div == 0)
			return div;
	}
	return -1;
}

void createJCoins(int j, int n) {
  for(unsigned int jcoin = (1 << n - 1) + 1;
      j > 0 && (jcoin & (1 << n - 1)); jcoin += 2) {
		bool isJCoin = true;
		int divs[10];
    for(int base = 2; base <= 10; base++) {
			long converted = convertJCoin(jcoin, n, base);
			divs[base - 2] = isPrime(converted);
			if(divs[base - 2] == -1) {
				isJCoin = false;
				break;
			}
    }
		if(isJCoin) {
			printJCoin(jcoin, n);
			for(int base = 2; base <= 10; base++)
				cout << " " << std::dec << divs[base - 2];
			cout << "\n";
			j--;
		}
  }
}

int main(int argc, char **argv) {
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    int j, n;
    cin >> n;
    cin >> j;
		cout << "Case #" << i << ":\n";
    createJCoins(j, n);
  }
  return 0;
}
