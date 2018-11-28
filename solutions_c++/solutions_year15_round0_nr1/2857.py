#include <iostream>
#include <cstdio>
#include <cstdlib> 
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxN = 1111;

char inp[maxN];
int Ntests, Smax, ID_test;

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	cin >> Ntests;
	while (Ntests) {
		Ntests--;
		cin >> Smax;
		cin >> inp;
		int i, num = 0, res = 0;
		for (i = 0; i <= Smax; i++) {
			res = max(res, i-num);
			num += inp[i]-48;
		}
		cout << "Case #" << (++ID_test) << ": " << res << endl;
	}
}