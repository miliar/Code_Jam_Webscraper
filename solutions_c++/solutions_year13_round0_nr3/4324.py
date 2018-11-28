#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
const int mr = 10000001;

long long seq[mr];
int cnt = 0;

inline bool ispal(long long x) {
	static char buf[100];
	sprintf(buf, "%lld", x);
	int l = strlen(buf);
	for (int i = 0; i < l / 2; ++i)
		if (buf[i] != buf[l - i - 1])
			return 0;
	return 1;
}

inline int count_le(long long x) {
	int r = upper_bound(seq, seq + cnt, x) - seq;
	return r;
}

int main() {
	ios::sync_with_stdio(0);

	for (int i = 0; i < mr; ++i) {
		if (ispal(i) && ispal((long long) i * i)) {
			seq[cnt++] = (long long) i * i;
		}
	}
//	for(int i=0;i<cnt;++i) {
//		cout <<i<<": " << seq[i]<<endl;
//	}
	int Tc;
	cin >> Tc;
	for (int Tn = 1; Tn <= Tc; ++Tn) {
		long long A, B;
		cin >> A >> B;
		long long ans = count_le(B) - count_le(A - 1);
		cout << "Case #" << Tn << ": " << ans << '\n';
	}
	return 0;
}
