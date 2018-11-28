#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int z_codejam_testcase;
#define SIZE(A) ((int)(A).size())
#define PB push_back
#define MP make_pair
#define gout printf("Case #%d: ", ++z_codejam_testcase), cout

int n;
long long p;

bool win(int n, long long k, long long p) {
	if (p <= 0) return 0;
	if (k == 0) return 1;
	return win(n-1, (k-1)>>1, p-(1LL<<(n-1)));
}

bool may(int n, long long k, long long p) {
	if (p >= (1LL<<n)) return k < p;
	if (p <= 0) return 0;
	if (k == 0) return 1;

	if (k == (1LL<<n)-1) return 0;

	return may(n-1, (k+1)>>1, p);
}

void main2() {
	cin >> n >> p;
	long long lo = 0, hi = (1LL<<n)-1, mi;
	for (; lo < hi;) {
		mi = (lo+hi+1)>>1;
		if (win(n, mi, p))
			lo = mi;
		else
			hi = mi-1;
	}
	gout << lo << " ";
	lo = 0; hi = (1LL<<n)-1;
	for (; lo<hi;) {
	 	mi = (lo+hi+1)>>1;
	 	if (may(n, mi, p))
	 		lo = mi;
	 	else
	 		hi = mi-1;
	}
	cout << lo << endl;
}




int main() {
	int test_num;
	scanf("%d", &test_num);
	for (; test_num--;) {
	 	main2();
	}


	return 0;
}
