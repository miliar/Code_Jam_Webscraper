#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "C",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);
 
int n, j, t;
int divisors[11];

void solve16() {
	for (int i = 0; i < j; i++) {
		string output = "11";
		int nr_bits = 2;
		for (int bit = 0; (1LL << bit) <= i; bit++, nr_bits += 2) {
			if ((1 << bit) & i)
				output += "11";
			else output += "00";			
		}

		for (; nr_bits != 14; nr_bits += 2) 
			output += "00";

		output += "11";

		fout << output << ' ';
		for (int i = 2; i <= 10; i++)
			fout << divisors[i] << ' ';
		fout << '\n';
	}
}

void solve32() {
	for (int i = 0; i < j; i++) {
		string output = "11";
		int nr_bits = 2;
		for (int bit = 0; (1LL << bit) <= i; bit++, nr_bits += 2) {
			if ((1 << bit) & i)
				output += "11";
			else output += "00";			
		}

		for (; nr_bits != 30; nr_bits += 2) 
			output += "00";

		output += "11";

		fout << output << ' ';
		for (int i = 2; i <= 10; i++)
			fout << divisors[i] << ' ';
		fout << '\n';
	}

}

int main() {
	fin >> t;
	fin >> n >> j;

	for (int i = 2; i <= 10; i++)
			divisors[i] = 1 + i;
	
	fout << "Case #1:\n";
	if (n == 16) 
		solve16();
	else solve32();
	return 0;
}