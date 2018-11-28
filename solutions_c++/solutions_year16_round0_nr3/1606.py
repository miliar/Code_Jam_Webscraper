#include<iostream>
#include<cmath>
#include<string>

using namespace std;

void findPrimes(long long n, long long* result) {
	result[1] = 2;
	result[2] = 3;
	result[3] = 5;
	
	long long i = 3;
	long long p = result[i] + 2;
	while(result[i] < n) {
		bool hasPrimeDivisor = false;
		for(long long j = 1; result[j] <= sqrt(p); j++) {
			if(p % result[j] == 0) {
				hasPrimeDivisor = true;
				break;
			}
		}
		if(!hasPrimeDivisor) {
			i = i + 1;
			result[i] = p;
		}
		p = p + 2;
	}
	result[0] = i;
}

string convertToBinary(long long n) {
	string result = "";
	string res1 = "";
	long long m = n;
	while(m > 0) {
		res1 += (char)(m % 2 + 48);
		m = m/2;
	}
	for(int i = res1.length()-1; i >= 0; i--) {
		result += res1[i];
	}
	return result;
}

string nextBinary(string num) {
	string result;
	string num1 = "0" + num;	
	int length = num1.length();
	int i = num1.length()-1;
	while(num1[i] != '0') {
		num1[i] = '0';
		i--;
	}
	num1[i] = '1';
	num1[num1.length()-1] = '1';
	if(num1[0] == '0') {
		result = num1.substr(1, length-1);
	} else {
		return num1;
	}
	
	return result;
}

long long findNModKInBaseB(string num, long long k, int b) {
	long long result = 0;
	int position = 0;
	long long variable = 0;
	int rem = b % k;
	for(int i = num.length()-1; i >= 0; i--) {
		variable = 1;
		if(num[i] == '0') {
			position++;
			continue;
		}
		for(int j = 1; j <= position; j++) {
			variable = ((variable % k) * (rem)) % k;
		}
		result = (result + variable) % k;
		position++;
	}
	
}

long long hasPrimeDivInBase(int base, string num, long long* primes) {
	for(int i = 1; i <= primes[0]; i++) {
		if(findNModKInBaseB(num, primes[i], base) == 0) {
			return primes[i];
		}
	}
	return -1;
}

string* setOfStrings(string num, long long* primes, int numOfStrings) {
	string num1 = num;
	int count = 0;
	string* result = new string[numOfStrings + 10];
	for(int i = 1; i <= numOfStrings; i++) {
		A:
		int primes1 [11];
		primes1[0] = 0;
		for(int j = 2; j <= 10; j++) {
			long long prime = hasPrimeDivInBase(j, num1, primes);
			if(prime == -1) {
				num1 = nextBinary(num1);
				goto A;
			}
			primes1[0]++;
			primes1[primes1[0]] = prime;
		}
		result[i] = num1;
		if(primes1[0] == 9) {
			count++;
			cout << num1;
			for(int g = 1; g <= 9; g++) {
				cout << " " << primes1[g];
			}
			cout << endl;
		}
		
		num1 = nextBinary(num1);
	}
	return result;
}

string getInitial(int length) {
	if(length == 1) {
		return "1";
	}
	if(length == 2) {
		return "11";
	}
	string res = "1";
	for(int i = 2; i < length; i++) {
		res += "0";
	}
	res += "1";
	return res;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output-large.txt", "w", stdout);

	
	long long* primes = new long long[999999];
	long long n = 32000;
	findPrimes(n, primes);

	int numOfTests;
	cin >> numOfTests;
	for(int i = 1; i <= numOfTests; i++) {
		int length, j;
		cin >> length >> j;
		string num = getInitial(length);
		cout << "Case #" << i << ":" << endl;
		string* result = setOfStrings(num, primes, j);
	}
	return 0;
}