#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

using ll = long long int;
ifstream fin("sheep.in");
ofstream fout("sheep.out");

void crossOut(ll n, ll& needToSee) {
	while (n) {
		needToSee &= ~(1 << (n % 10));
		n /= 10;
	}
}

int main() {
	ll T, N;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fin >> N;
		
		fout << "Case #" << t << ": ";

		if (N == 0) {
			fout << "INSOMNIA" << endl;
			continue;
		}

		ll needToSee = 1023;
		ll cur = 0;

		while (needToSee)
			crossOut(cur += N, needToSee);

		fout << cur << endl;
	}
}
