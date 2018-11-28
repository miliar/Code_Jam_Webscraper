#include <iostream>
#include <sstream>
#include <string>
using namespace std;
class Sheep {
  private:
	bool* digits;
	int base, num;
	bool asleep;
  public:
	void updateDigits(void) {
		string nstr = to_string(num);
		int l = nstr.length();
		int c;
		for(int i = 0; i < l; i++) {
			c = (int)nstr[i];
			if(c > 47 && c < 58)
				digits[c-48] = true;
		}
	}
	bool checkDigits(void) {
		int s = 0;
		for(int i = 0; i < 10; i++) {
			if(digits[i])
				s++;
		}
		return (s == 10);
	}
	/*
	void printDigits(void) {
		for(int i = 0; i < 10; i++) {
			cout << i << ':' << digits[i] << ' ';
		}
		cout << endl;
	}
	*/
	void doCount(void) {
		num += base;
		updateDigits();
		asleep = checkDigits();
	}
	int runCase(void) {
		while(!asleep) {
			doCount();
		}
		return num;
	}
	Sheep(int n) {
		base = n;
		num = n;
		asleep = (n == 0);
		digits = new bool[10];
		for(int i = 0; i < 10; i++) {
			digits[i] = false;
		}
		updateDigits();
	}
};

int main(void) {
	int cases, N, cres;
	cin >> cases;
	for(int i = 0; i < cases; i++) {
		cin >> N;
		Sheep sh(N);
		cres = sh.runCase();
		cout << "Case #" << i+1 << ": ";
		if(cres == 0)
			cout << "INSOMNIA";
		else
			cout << cres;
		cout << endl;
	}
}