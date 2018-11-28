#include <iostream>
#include <fstream>
using namespace std;

#define cout fout

ofstream fout("c.out");

const long long MAXN = 100000;
bool mk[MAXN];
long long primes[MAXN];
long long nPrimes;
long long result;

void genPrimes() {
	long long curr = 4, i;
	for (i = 2; curr < MAXN; i++, curr += i + i + 1) {
		if (!mk[i]) {
			primes[nPrimes++] = i;
			
			for (long long k = curr; k < MAXN; k += i) {
				mk[k] = true;
			}
		}
	}
	
	while (i < MAXN) {
		if (!mk[i]) {
			primes[nPrimes++] = i;
		}
		
		i++;
	}
}

long long getFactor(int n[], long long b) {
	long long num = 0;
	for (int i = 0; i < 16; i++) {
		num *= b;
		num += n[i];		
	}
	
	for (long long i = 0; i < nPrimes && primes[i] * primes[i] <= num; i++) {
		if (num % primes[i] == 0) {
			/*
			if (b ==10) {
				cout << ' ' << num << ' ' << i << ' ' << primes[i] << endl;
			}
			* */
			//cout << ' ' << num << ' ' << i << ' ';
			return primes[i];
		}
	}
	
	return -1;
}

void getResult(int n[]) {
	long long factors[11];
	
	for (long long i = 2; i < 11; i++) {
		factors[i] = getFactor(n, i);
		
		if (factors[i] < 0) {
			return;
		}
	}
	
	for (int i = 0; i < 16; i++)
		cout << n[i];
	
	for (long long i = 2; i < 11; i++) {
		cout << ' ' << factors[i];
	}
	cout << endl;
	
	result++;
}


int seq[16];
void genSeq(int n) {
	if (result == 50)
		return;
		
	if (n == 15) {
		getResult(seq);
		return;
	}
	
	seq[n] = 0;
	genSeq(n + 1);
	
	seq[n] = 1;
	genSeq(n + 1);
}

int main() {
	cout << "Case #1:" << endl;
	genPrimes();
	
	seq[0] = seq[15] = 1;
	genSeq(1);
	/*
	for (long long i = 1000000000000001L; i <= 1111111111111111L && result < 50; i += 10) {
		getResult(i);
	}
	* */
	
	//cout << result;
	
	/*
	for (long long i = 0; i < 100; i++) {
		cout << primes[i] << endl;
	}
	
	cout << nPrimes << endl;
	* */
	
	return 0;
}

