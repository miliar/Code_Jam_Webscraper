#include <fstream>

using namespace std;

long long mpy(long long n, long long p) {
	if(n == 1) return 1;
	if(n == p) return p;
	return mpy(n / 2, p / 2 + 1);
}

long long mpz(long long n, long long p) {
	if(n == 1) return 1;
	if(p == 1) return 1;
	return mpz(n / 2,(p - 2) / 2 + 1) + n / 2;
}

int main() {
	ifstream fin("b.in");
	ofstream fout("b.out");
	int t, n, x;
	long long p;
	fin >> t;
	for(x = 1; x <= t; x++) {
		fin >> n >> p;
		fout << "Case #" << x << ": " << mpy(1 << n, p) << mpz(1 << n, p) << "\n";
	}
	return 0;
} 
