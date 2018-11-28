#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <set>
#include <cassert>
#include <cmath>

using namespace std;

ifstream fin ("b.in");
ofstream fout ("b.out");

long long int T, N, P;

int log2(long long int x) {
	float y = log(x) / log(2);
	return floor(y + 0.000000001);
}

int main () {
	fin >> T;
	for (long long int i =  1; i <= T; i++) {
		fout << "Case #" << i << ": ";
		fin >> N >> P;
		//cout << "N = " << N << "\nP = " << P << "\n";
		if (P == ((long long int) 1) << N) {
			fout << P-1 << ' ' << P-1 << '\n';
			continue;
		}
		int j = 0;
		long long int een = 1;
		while ((een << N) - (een << N-j) + 1 <= P) {
			j++;
		}
		//cout << "j = " << j << '\n';
		fout << (een << j) - 2;		
		long long int ans = (een << N) - (een << (N - log2(P)));
		fout << ' ' << ans << '\n';
		//cout << '\n';
	}	
	return 0;
}
