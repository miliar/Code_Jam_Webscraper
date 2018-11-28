#pragma comment(linker,"/stack:256000000")

#include <cmath> 
#include <ctime> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <cstring> 
#include <cstdlib> 
#include <queue> 
#include <cstdio> 
#include <cfloat>

using namespace std; 

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++) 
#define sz(v) (int)(v).size() 
#define all(v) (v).begin(), (v).end()

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tst;
	scanf("%d", &tst);	
	REP(_, tst) {
		int n;
		long long p;
		cin >> n >> p;
		long long low = 0, high = 0, a = -1, b = -1;
		for (int L = 0; L <= n; L++) {
			if (L > 0) {
				low += (1LL << (n - L));
				high += (1LL << (L - 1));
			}
			if (low >= p && a == -1) a = L - 1;
			if (high >= p && b == -1) b = L - 1;
		}
		if (a == -1) a = n;
		if (b == -1) b = n;
		a = (1LL << (a + 1)) - 2;
		b = (1LL << n) - (1LL << (n - b));
		a = min(a, (1LL << n) - 1);
		b = min(b, (1LL << n) - 1);
		cout << "Case #" << _ + 1 << ": " << a << " " << b << endl;
	}
	return 0;
}