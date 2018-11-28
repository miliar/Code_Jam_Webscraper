#include <bits/stdc++.h>

using namespace std;

int check_prime(long long int N) {
	if(N <= 1) return 0;

	for(int i = 2, sqrt_N = sqrt(N); i <= sqrt_N; i++)
		if(N%i == 0)
			return 0;
	return 1;
}


long long int get_num(string &s, int base, int size) {
	long long int ret = 0;
	long long int multi = 1;

	for(int i = size-1; i >= 0; i--) {
		if(s[i] == '1') {
			ret += multi;
		}
		multi *= base;
	}

	return ret;
}

long long int pot(long long int base, int expo) {
	long long int ret = 1;
	while(expo--)
		ret *= base;
	return ret;
}

void solve(int N, int J) {
	string s;
	for(int i = 0; i < N; i++)
		s+='0';
	s[0] = s[N-1] = '1';

	long long int bases[11];
	long long int divisors[11];
	long long int i_cpy, k;
	long long int pow_2t = pot(2, N-2);
	int prime;

	for(long long int i = 0; i < pow_2t; i++) {
		i_cpy = i;
		for(int j = 1; j < N-1; j++) {
			s[N-j-1] = i_cpy%2 + '0';
			i_cpy /= 2;
			//cout << N-j << endl;
		}

		prime = 0;
		for(int j = 2; j <= 10; j++) { //check if primes
			bases[j] = get_num(s, j, N);
			if(check_prime(bases[j])) {
				prime = 1;
				break;
			}
		}

		if(!prime) { //check trivial divisors
			for(int j = 2; j <= 10; j++) {
				for(k = 2; k < bases[j]; k++)
					if(bases[j]%k == 0) {
						divisors[j] = k;
						break;
					}
				if(k == bases[j]) {
					prime = 0;
					break;
				}
			}
		}

		if(!prime) {
			J--;
			cout << s;
			for(int j = 2; j <= 10 ; j++)
				cout << " " << divisors[j];
			cout << endl;

			if(J == 0)
				break;
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	int T, N, J;

	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> N >> J;
		cout << "Case #" << i+1 << ":" << endl;
		solve(N, J);
	}

	return 0;
}