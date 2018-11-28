#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <cmath>
#include <bitset>
#include <list>
#include <queue>

using namespace std;

#define e '\n'
#define INF 1023456789
#define ll long long

//#define FILE "myFile"

#ifdef FILE
ifstream f(string (string(FILE) + ".in").c_str());
ofstream g(string (string(FILE) + ".out").c_str());
#endif
#ifndef FILE
#define f cin
#define g cout
#endif

ll mul_inv(ll a, ll b)
{
	ll b0 = b, t, q;
	ll x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

string s;
long long t;
int i, j, ii;
map<char, int> mp;
map<int, int> rez;

void subtract(string number, int n) {
	for (i = 0; i < number.length(); i++) {
		mp[number[i]] -= n;
	}
}

int main() {
	f >> t;

	for (int ii = 1; ii <= t; ii++) {
		f >> s;

		mp.clear();
		rez.clear();

		for (i = 0; i < s.length(); i++ ){
			mp[s[i]]++;
		}

		rez[0] += mp['Z'];
		rez[2] += mp['W'];
		rez[4] += mp['U'];
		rez[6] += mp['X'];
		rez[8] += mp['G'];

		subtract("ZERO", rez[0]);
		subtract("TWO", rez[2]);
		subtract("FOUR", rez[4]);
		subtract("SIX", rez[6]);
		subtract("EIGHT", rez[8]);

		rez[1] += mp['O'];
		rez[3] += mp['H'];
		rez[5] += mp['F'];
		rez[7] += mp['S'];

		subtract("ONE", rez[1]);
		subtract("THREE", rez[3]);
		subtract("FIVE", rez[5]);
		subtract("SEVEN", rez[7]);

		rez[9] += mp['E'];

		g << "Case #" << ii << ": ";
		for (i = 0; i <= 9; i++ ){
			for (j = 1; j <= rez[i]; j++) {
				g << i;
			}
		}
		g << e;

	}

}

