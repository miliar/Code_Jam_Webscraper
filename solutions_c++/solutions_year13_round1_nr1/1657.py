#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define pb push_back
#define sz(a) int((a).size()
#define all(c) (c).begin(),(c).end()

unsigned long long search (unsigned long long t, unsigned long long r, unsigned long long start, unsigned long long end) {
	unsigned long long n = (end + start) / 2;
	if ((2*r-1)*n + 2*n*n <= t && t < (2*r-1)*(n+1) + 2*(n+1)*(n+1)) {
		return n;
	}
	else {
		if ((2*r-1)*n + 2*n*n <= t) {
			return search(t, r, n, end);
		}
		else return search (t, r, start, n);
	}
}

int main () {
	unsigned long long int T, c, r, t;
	fin >> T;

	for (c = 1; c <= T; c++) {
		fin >> r >> t;

		fout << "Case #" << c << ": " << search(t, r, 0, (unsigned long long) 10000000000) << endl;
	}

}
