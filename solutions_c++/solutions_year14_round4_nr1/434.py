#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <string>
using namespace std;

//#define in cin
//#define out cout

ifstream in("A-large.in.txt");
ofstream out("A-large-out");
int T, N, X;
int S[705];

int main()
{
	in >> T;
	for (int cnt = 1; cnt <= T; cnt++) {
		in >> N >> X;
		int ss;
		memset(S, 0, sizeof(S));
		for (int i = 0; i < N; i++) {
			in >> ss;
			S[ss]++;
		}
		int res = 0;
		int i = X;
		while (i >= 1) {
			if (S[i] == 0) {
				i--;
				continue;
			}
			int j = min(X-i, i);
			for ( ; j >= 1; j--) {
				if (S[j] > 0) {
					int t = min(S[j], S[i]);
					if (i == j) t = t/2;
					S[j] -= t;
					S[i] -= t;
					res += t;
					if (S[i] == 0) {
						break;
					}
				}
			}
			if (S[i]) {
				res += S[i];
				S[i] = 0;
			}
			i--;
		}
		out << "Case #" << cnt << ": " << res << endl;
	}
	return 0;
}