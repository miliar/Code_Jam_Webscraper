#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <cstring>
#include <sstream>
#include <algorithm>

using namespace std;

unsigned long long interpret_base(unsigned long long n, unsigned long long base) {
    unsigned long long value = 0;
    unsigned long long mult = 1;
    while (n > 0) {
        value += (n & 1) * mult;
        mult *= base;
        n >>= 1;
    }
    return value;
}

string to_binary_string(unsigned long long v) {
    stringstream ss;
    while (v) {
        ss << (v&1);
        v >>= 1;
    }
    string s = ss.str();
    reverse(&s[0], &s[0] + s.size());
    return s;
}

long long find_divisor(long long num, vector<long long> &primes) {
    long long limit = sqrt(num);
    for (long long i = 0; i < primes.size() && primes[i] <= limit; i++) {
        if (num % primes[i] == 0) {
            return primes[i];
        }
    }
    return -1;
}

vector<long long> get_primes(long long P)
{
	vector<long long> primes;
	long long sievebound = (P-1)/2;
	long long crossbound = ((long long)sqrt((double)P)-1)/2;
	bool *sieve = new bool[(P-1)/2+1];
    memset(sieve, 0, (P-1)/2+1);
	for (long long i = 1; i <= crossbound; i++)
		if (!sieve[i])
			for (long long j = 2*i*(i+1); j <= sievebound; j += 2*i+1)
				sieve[j] = 1;
	primes.push_back(2);
	for (long long i = 1; i <= sievebound; i++)
		if (!sieve[i])
			primes.push_back(2*i+1);
	delete [] sieve;
	return primes;
}

int main() {
    long long T;
    cin >> T;
    vector<long long> primes = get_primes(1<<16);
    for (long long t = 1; t <= T; t++) {
        cout << "Case #" << t << ":\n";

        long long N, J;
        cin >> N >> J;

        long long max = (1 << N)-1;
        long long min = (1 << (N-1)) + 1;
        for (long long i = min; i <= max; i += 2) {
            bool valid = true;
            vector<long long> divisors;
            for (long long j = 2; j <= 10; j++) {
                long long val = interpret_base(i, j);
                long long div = find_divisor(val, primes);
                if (div == -1) {
                    valid = false;
                    break;
                }
                divisors.push_back(div);
            }
            if (valid) {
                cout << to_binary_string(i);
                for (long long k = 0; k < divisors.size(); k++) {
                    cout << " " << divisors[k];
                }
                cout << "\n";
                if (--J <= 0) {
                    exit(1);
                }
            }
        }
    }
}
