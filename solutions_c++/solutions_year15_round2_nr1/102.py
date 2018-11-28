#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

long reverse(long n)
{
	long ret = 0;
	while (n > 0) {
		ret = ret * 10 + n%10;
		n /= 10;
	}
	return ret;
}

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
		long N, cnt = -1;
		cin >> N;
		while (N > 0) {
			long dcnt = log10(N);
			dcnt = dcnt/2 + 1;
			long ten = 1;
			forn(i, dcnt) ten *= 10;
			//cout << ten << " <= 10" << endl;
			if (N%ten == 0) {
				--N;
				++cnt;
				continue;
			}
			if (N%ten > 1) {
				cnt += N%ten - 1;
				N = N - (N%ten - 1);
			} 
			//cout << N << " <- 1" << endl;
			if (reverse(N) < N) {
				N = reverse(N);
				++cnt;
				//cout << N << " <- 2" << endl;
			} else {
				N -= 2;
				cnt += 2;
				//cout << N << " <- 3" << endl;
			}
		}

		cout << "Case #" << casenum << ": " << cnt << endl;
	}
	return 0;
}

