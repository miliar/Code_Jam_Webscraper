#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <cstdlib>
#include <iostream>

using namespace std;

int T;
long long A, B;

inline bool isPalin(long long a) {
	long long b = a, rev = 0;
	while (b > 0) {
		rev = rev * 10 + (b % 10);
		b /= 10;
	}
	return (a == rev);
}

set<long long> st;

inline void process() {
	for(long long i = 1 ; i <= 10000000 ; i++) {
		if (isPalin(i) && isPalin(i * i)) {
			//cout << (i * i) << endl;
			st.insert(i * i);
		}
	}
}

int main() {
	process();
	vector<long long> v(st.begin(), st.end());
	scanf("%d", &T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%lld %lld", &A, &B);
		long long ans = 0;
		for(int i = 0 ; i < (int)v.size() ; i++)
			if (v[i] >= A && v[i] <= B)
				ans++;
		printf("Case #%d: %lld\n", t, ans);
	}
}
