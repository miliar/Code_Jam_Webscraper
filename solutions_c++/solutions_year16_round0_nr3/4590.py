#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//to solve large version of this problem, I'd need to use
//external big int library
typedef unsigned long long lint;

//given a 1/0 string in a certain base, convert value to base 10
lint interpret(string jamcoin, int base) {
	lint r = 0;
	lint baseModifier = 1;
	for(string::reverse_iterator it = jamcoin.rbegin();
		it != jamcoin.rend();
		++it) {
		if(*it == '1') {
			r += baseModifier;
		}
		baseModifier *= base;
	}
	return r;
}

//my solution to this problem is probalistic...
//for better results, increase number of loops
lint naiveLazyPrime(lint n) {
	for(lint i = 2; i < n/2 && i < 10000; ++i)
		if(n % i == 0)
			return i;
	return 0;
}

void incrementJamCoin(string& s) {
	for(string::reverse_iterator rit = s.rbegin() + 1;
		rit != s.rend();
		++rit) {
		if(*rit == '0') {
			*rit = '1';
			break;
		} else {
			*rit = '0';
		}
	}
}

//is this a jamcoin
bool evaluateCoin(string coin) {
	for(int base = 2; base <= 10; ++base) {
		lint bten = interpret(coin, base);
		lint divisor = naiveLazyPrime(bten);
		if(divisor == 0) {
			return false;
		}
	}
	return true;
}

//print jamcoin's divisors
bool printCoin(string coin, ofstream& os) {
	os << coin;
	for(int base = 2; base <= 10; ++base) {
		lint bten = interpret(coin, base);
		os << " " << naiveLazyPrime(bten);
	}
	os << endl;
}


int main(int argc, char* argv[]) {
	//j jamcoins of length n
	const int n = 16;
	const int j = 50;

	ofstream os("out.txt");
	os << "Case #1:" << endl;

	string jamcoin = "1000000000000001";
	int jamCoinsFound = 0;
	while(jamcoin.compare("0000000000000001") != 0
		&& jamCoinsFound < j) {
		if(evaluateCoin(jamcoin)) {
			printCoin(jamcoin, os);
			++jamCoinsFound;
		}
		incrementJamCoin(jamcoin);
	}
}