#include <iostream>
#include <bitset>
#include <math.h>

using namespace::std;

typedef __uint128_t uint128_t;

#define MAXPRIME 100000
#define N 32
#define J 500

int primes[MAXPRIME] = {0};
int num_of_primes = 0;

//generate a bunch of prime numbers
void generate_primes() {
	int seive[MAXPRIME] = {0};
	for (int i=2; i< MAXPRIME; i++) {
		seive[i] = 1;
	}
	for (int i=2; i<sqrt(MAXPRIME); i++) {
		for (int j=i*i; j<MAXPRIME; j+=i) {
			seive[j] = 0;
		}
	}
	for (int i=2; i< MAXPRIME; i++) {
		if (seive[i]==1) {
			primes[num_of_primes] = i;
			num_of_primes++;
		}
	}
}

//test for prime. this is not an exhaustive search
//but should get the low hanging ones
long long get_divisor(uint128_t num) {
	int reminder = 0;
	for(int i=0; i<num_of_primes; i++) {
		if(primes[i] >= num)
			return -1;

		reminder = num % primes[i];
		if (reminder == 0)
			return primes[i];
	}
	return -1;
}

//print 128bit integer
string num_to_string(uint128_t num) {
	int reminder = 0;
	string output;

	while (num != 0) {
		reminder = num % 10;
		output =  to_string(reminder) + output;
		num = num / 10;
	}
	return output;
}

//calculate b^position
uint128_t power(int digit, int position, int base) {
	uint128_t res = 1;
	for(int i=0; i<position; i++) {
		res = (uint128_t)res * (uint128_t)base;
	}
	return res;
}

//convert string to base representation
uint128_t get_interpretation(string input, int base) {
	uint128_t res = 0;
	int length = input.length();

	for(int i=0; i<length; i++) {
		if (input[i] == '1') {
			res += power(1, length-i-1, base);
		}
	}
	return res;
}

//generate jamcoin
string generate_jamcoin(int n) {
	string x = "1" + bitset<N-2>(n).to_string() + "1";
	return x;
}

//test if this is a valid jamcoin
//generate divisors
bool test_jamcoin(string jamcoin, uint128_t interpret[], long long divisor[]) {
	uint128_t num = 0;
	long long result = 0;

	for(int base=2; base<=10; base++) {
		num = get_interpretation(jamcoin, base);
		result = get_divisor(num);
		if(result == -1) {
			//we may have encountered a prime number
			//we can abort checking this jamcoin
			return false;
		}
		interpret[base] = num;
		divisor[base] = result;
	}
	return true;
}

void coin_jam() {
	string jamcoin = "";
	uint128_t interpret[12];
	long long divisor[12];
	int counter = 0;

	for(int i=0;;i++) {
		jamcoin = generate_jamcoin(i);
		if(test_jamcoin(jamcoin, interpret, divisor)) {
			counter++;
			cout << jamcoin << " ";
			for (int base=2; base<=10; base++) {
				cout << divisor[base];
				if(base != 10)
						cout << " ";
			}
			cout << endl;
		}
		if(counter >= J)
			return;
	}
}

int main() {
	cout << "Case #1:"  << endl;
	generate_primes();
	coin_jam();

	return 0;
}
