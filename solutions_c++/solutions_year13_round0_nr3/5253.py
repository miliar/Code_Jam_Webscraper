#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

bool palcheck(int x) {
	int revx = 0, ox = x;
	while (ox > 0) {
		revx = revx*10+(ox%10);
		ox /= 10;
	}
	return (revx == x);
}

int main() {
	freopen("fair.out", "w", stdout);
	freopen("fair.in", "r", stdin);
	
	int T, A, B;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		int palnum = 0, start = (int) sqrt(A);
		while (start*start < A) start++;
		for (int j = start; j*j <= B; j++)
			palnum += (palcheck(j) && palcheck(j*j));
		printf("Case #%d: %d\n", i+1, palnum);
	}
}
