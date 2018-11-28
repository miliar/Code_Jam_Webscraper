#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <list>
#include <algorithm>
using namespace std;

typedef unsigned int uint; // 0 - 4.294.967.295 (4.29 * 10^10)
typedef long long ll; // 0 - 89.223.372.036.854.775.807i64 (8.92 * 10^19)
typedef unsigned long long ull; // 0 - 818446744073709551615i64 (8.18 * 10^20)
typedef vector<int> vi;
typedef vector<ll> vll;

#define REP(n) for(int i=0;i<n;i++)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORAB(i,a,b) for(int i=a;i<=b;i++)
#define FORCHR(str, c) for(string::size_type c = 0; c < str.length(); c++)
#define FOREACH(c, it) for (auto it = (c).begin(); it != (c).end(); it++)
#define RESET(obj, val) memset(obj, val, sizeof obj)

string input_file = "C-small-attempt0.in";

bool pal[9][10000];
char str[21];

bool palindrome(ull num) {
	sprintf(str, "%llu", num);
	int cifre = strlen(str);
	int meta = (cifre + (cifre % 2)) / 2;
	FOR(c, meta) {
		if (str[c] != str[cifre - c - 1]) return false;
	}
	return true;
}

int reversen(int n) {
	int reverse = 0;
	while(n != 0) {
		int digit = n % 10; //modulo
		reverse = (reverse * 10) + digit;
		n /= 10;
	}
	return reverse;
}

void precalcola() {
	FORAB(c, 1, 8) {
		int cifre = (int)(c + c % 2) / 2;
		int startn = 1;
		REP(cifre - 1) {
			startn *= 10;
		}
		int endn = startn + (startn * 9) - 1;
		FORAB(n, startn, endn) {
			ull fulln = n;
			if (c > 1) {
				if (c % 2 == 1) fulln -= fulln % 10;
				REP(c - cifre) {
					fulln *= 10;
				}
				// Reverse number
				fulln += reversen(n);
			}
			pal[c][n] = palindrome(fulln * fulln);
		}
	}
}

int digits(ull n) {
	int d = 0;
    while (n) {
        n /= 10;
        d++;
    }
    return d;
}

int getpalprefix(ull n, int digits) {
	int cifre = (digits + (digits % 2)) / 2;
	REP(digits - cifre) {
		n /= 10;
	}
	return (int) n;
}

ull nextpalindrome(ull num) {
	if (num == 9) return 11;
	if (num < 9) return num + 1;

	int d = digits(num);
	int prefix = getpalprefix(num, d);

	ull newpal = (ull)prefix;
	if (d % 2 == 1) newpal -= newpal % 10;
	int cifre = (d + (d % 2)) / 2;
	REP(d - cifre) {
		newpal *= 10;
	}
	newpal += reversen(prefix);

	if (newpal > num) return newpal;

	prefix++;
	newpal = (ull)prefix;
	if (d % 2 == 1) newpal -= newpal % 10;
	cifre = (d + (d % 2)) / 2;
	REP(d - cifre) {
		newpal *= 10;
	}
	return newpal + reversen(prefix);
}

ull previouspalindrome(ull num) {
	if (num == 11) return 9;
	if (num < 11) return num - 1;

	int d = digits(num);
	int prefix = getpalprefix(num, d);

	ull newpal = (ull)prefix;
	if (d % 2 == 1) newpal -= newpal % 10;
	int cifre = (d + (d % 2)) / 2;
	REP(d - cifre) {
		newpal *= 10;
	}
	newpal += reversen(prefix);

	if (newpal < num) return newpal;

	prefix--;
	newpal = (ull)prefix;
	if (d % 2 == 1) newpal -= newpal % 10;
	cifre = (d + (d % 2)) / 2;
	REP(d - cifre) {
		newpal *= 10;
	}
	return newpal + reversen(prefix);
}



ll solve(ull A, ull B) {
	// Passa alle radici quadrate di A e B
	ull minsqrt = (ull) ceill(sqrtl((long double)A));
	ull maxsqrt = (ull) floorl(sqrtl((long double)B));

	// Limite massimo di valisità di questo algoritmo
	if (maxsqrt > 10000000) return -1;

	
	// Cerca il primo palindromo disponibile
	ull firstpal = palindrome(minsqrt)? minsqrt : nextpalindrome(minsqrt);
	int c0 = digits(firstpal);
	int startn = getpalprefix(firstpal, c0);
	
	// Calcola l'ultimo palindromo da controllare
	ull lastpal = palindrome(maxsqrt)? maxsqrt : previouspalindrome(maxsqrt);
	int c1 = digits(lastpal);
	int endn = getpalprefix(lastpal, c1);

	if (firstpal > maxsqrt || lastpal < minsqrt) return 0;

	ll howmuch = 0;
	if (c0 == c1) {
		FORAB(n, startn, endn) {
			if (pal[c0][n]) howmuch++;
		}
	}
	else {
		int cifre0 = (c0 + (c0 % 2)) / 2;
		int endn0 = (cifre0 * 10) - 1;
		FORAB(n, startn, endn0) {
			if (pal[c0][n]) howmuch++;
		}
		FORAB(c, c0 + 1, c1 - 1) {
			int cifre = (c + (c % 2)) / 2;
			int startnc = 1;
			REP(cifre - 1) {
				startnc *= 10;
			}
			int endnc = (cifre * 10) - 1;
			FORAB(n, startnc, endnc) {
				if (pal[c][n]) howmuch++;
			}
		}
		int cifre1 = (c1 + (c1 % 2)) / 2;
		int startn1 = 1;
		REP(cifre1 - 1) {
			startn1 *= 10;
		}
		FORAB(n, startn1, endn) {
			if (pal[c1][n]) howmuch++;
		}
	}

	return howmuch;
}

int main() {
	freopen(input_file.c_str(), "r", stdin);
	string output_file = input_file.substr(0, input_file.find_last_of('.')) + ".out";
	freopen(output_file.c_str(), "w", stdout);

	int ntc;
	ull A, B;
	//cout.precision(6);
	//cout.setf(ios::fixed);

	precalcola();

	cin >> ntc;
	FORAB(tc, 1, ntc) {
		cin >> A >> B;
		cout << "Case #" << tc << ": " << solve(A, B) << endl;
	}
	return EXIT_SUCCESS;
}