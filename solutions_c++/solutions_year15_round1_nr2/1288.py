#include <cassert>
#include <fstream>
#include <set>
#include <utility>
using namespace std;

long long gcd(long long a, long long b) {
	while (b!=0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}

long long lcm(long long a, long long b) {
	return (a / gcd(a, b)) * b;
}

struct comp {
	bool operator() (const pair<long long, int> &a, const pair<long long, int> &b) const {
		return (a.first < b.first || (a.first == b.first && a.second < b.second));
	} 
};

int getAns(const int m[], int B, long long n) {
	long long totLcm = 1;
	for (int i=0; i<B; i++) 
		totLcm = lcm(totLcm, m[i]);

	long long oneRound = 0;
	for (int i=0; i<B; i++) 
		oneRound += totLcm / m[i];

	n = n % oneRound;
	if (n == 0) 
		n = oneRound;

	if (n <= B) {
		return n;
	}

	set< pair<long long, int>, comp> state;
	for (int i=0; i<B; i++) {
		state.insert(make_pair((long long) m[i], i));
	}

	for (long long i=B+1; i<n; i++) {
		set< pair<long long, int>, comp >::iterator min = state.begin();
		int k = min->second;
		long long t = min->first;
		state.erase(min);
		state.insert(make_pair(t+m[k], k));
	}

	return state.begin()->second + 1;
}

int main() {
	ifstream fin("B-small-attempt0.in");
	ofstream fout("pb-small.out");
	assert(fin && fout);
	int test;
	fin >> test;
	for (int count=1; count<=test; count++) {
		int B;
		long long n;
		fin >> B >> n;
		int m[B];
		for (int i=0; i<B; i++) {
			fin >> m[i];
		}
		fout << "Case #" << count << ": " << getAns(m, B, n) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}