/*
LANG: C++
ID: he.andr1
PROG: C
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<cstring>
#include<cassert>
#include<stack>
#include<list>
#include<cstdio>
#include<numeric>
#include<complex>
#include<string>
#include<map>

using namespace std;

#define DEBUG 1

#ifdef DEBUG
	#define ERR cerr
#else
	#define ERR if(true); else cerr
#endif

#define ITER(v, i) for(__typeof(v.begin()) i = v.begin(); i != v.end(); i++) 
#define X real()
#define Y imag()
#define A first
#define B second

typedef pair<int, int> pii;
typedef complex<int> pt;
typedef long long ll;

template <class T> T cross(complex<T> a, complex<T> b) { return imag(a * conj(b)); }

template <class T> T min(T a, T b, T c) { return min(a, min(b, c)); }

template <class T> T max(T a, T b, T c) { return max(a, max(b, c)); }

template <class T> void setmin(T &a, T b) { if(b < a) a = b; }

template <class T> void setmax(T &a, T b) { if(b > a) a = b; }

bool isPalindrome(int n) {
	if(n == 0) return true;
	if(n < 0) return false;
	string s;
	for(; n > 0; n /= 10) s = ((char) (n % 10)) + s;
	for(int i = 0, j = s.length() - 1; i < j; i++, j--) {
		if(s[i] != s[j]) return false;
	}
	return true;
}

void io(istream &in, ostream &out) {
	int T; 
	in >> T;
	for(int z = 1; z <= T; z++) {
		int A, B;
		in >> A >> B;
		int ans = 0;
		for(int i = 1; i * i <= B; i++) {
			if(i * i < A) continue;
			if(isPalindrome(i) && isPalindrome(i * i)) ans++;
		}
		out << "Case #" << z << ": " << ans << '\n';
	}
}

int main() {
	ifstream fin ("C-small-attempt0.in");
	if(fin.good()) {
		ofstream fout ("C-small-attempt0.out");
		io(fin, fout);
		fin.close();
		fout.close();
	} else 
		io(cin, cout);
	return 0;
}
