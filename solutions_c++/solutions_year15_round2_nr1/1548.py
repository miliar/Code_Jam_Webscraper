#include <fstream>
#include <cassert>
using namespace std;

const long long maxN = 1000001;

long long reverse(long long x) {
	long long rev = 0;
	while (x > 0) {
		int r = x % 10;
		rev = rev * 10 + r;
		x /= 10;
	}
	return rev;
}

void preprocess(long long a[]) {
	fill_n(a, maxN+1, 0);
	a[1]=1;
	for (long long i=2; i<=maxN; i++) {
		a[i] = a[i-1] + 1;
		if (i % 10 != 0) {
			long long j = reverse(i);
			if (j < i) 
				a[i] = min(a[i], a[j]+1);
		}
	}
}

int main() {
	long long a[maxN+1];
	preprocess(a);

	ifstream fin("A-small-attempt0.in");
	ofstream fout("pa-small.out");
	assert(fin && fout);
	int test;
	fin >> test;
	for (int count=1; count<=test; count++) {
		long long n;
		fin >> n;
		assert(n <= maxN);
		fout << "Case #" << count << ": " << a[n] << endl;
	}
	fin.close();
	fout.close();
	return 0;
}