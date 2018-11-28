#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#define INF 1000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;

long long N;
long long P;

long long a2(long long x) {
	long long count = -1;
	while (x != 0) {
		count++;
		x /= 2;
	}
	long long sum = 0;
	for (long long i = 0; i < count; i++) {
		sum += 1 << (N-1-i);
	}
	return sum;
}

int main() {
	int nCases;
	cin >> nCases;
	for (int cnum = 1; cnum <= nCases; cnum++) {
		cin >> N >> P;
		ll sol2 = a2(P);
		ll a1 = 0;
		if (P == (1 << N)) {
			a1 = (1 << N)-1;
		} else {
			int count = 1;
			P--;
			while (P - (1 << (N-count)) >= 0) {
				P -= (1 << (N-count));
				a1 += (1 << count);
				count++;
			}
		}
		cout << "Case #" << cnum << ": " << a1 << " " << sol2 << endl;
	}
}
