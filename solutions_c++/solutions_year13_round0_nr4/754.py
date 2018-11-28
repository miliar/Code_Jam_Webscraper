#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;
typedef unsigned long long ULL;

int K, N;
int keycnt[25][205];	// keycnt[i][t] := keys of type 't' held in chest 'i'; i = 0 is initial state
int type[25];		// type[i] := key type required to open chest 'i', 1 <= i <= N

ULL factorial[25];
ULL p[(1<<20)+5];	// p[s] := permutation code corresponding to lex min path to set 's' of remaining chests
			// E.g. if N=7 and it takes path 1,3,2 to reach a state 's', then p[s] ~ (1,3,2,4,5,6,7)

void reset_vars() {
	for (int i = 0; i <= N; i++)
		for (int j = 1; j <= 200; j++)
			keycnt[i][j] = 0;
	for (int i = 1; i <= N; i++)
		type[i] = -1;
	for (int s = 0; s < (1<<N); s++)
		p[s] = (ULL)-1;
	factorial[0] = 1;
	for (int i = 1; i <= 20; i++)
		factorial[i] = i * factorial[i-1];
	//for (int i = 0; i <= 20; i++) cout << i << "! = " << factorial[i] << endl;
}

int set_size(int s) {
	int cnt = 0;
	for (int i = 0; i < N; i++)
		if (s & (1<<i))
			cnt++;
	return cnt;
}

void compute_result() {
	p[(1<<N)-1] = 0;
	for (int r = N-1; r >= 0; r--)
		for (int s = 0; s < (1<<N); s++) if (set_size(s) == r) {
			//cout << "r = " << r << "; s = " << s << endl;
			// 's' represents a set of 'r' remaining chests to open
			int mj = 0;
			ULL mp = (ULL)-1;
			int j = 0;
			for (int e = 0; e < N; e++) {
				if (s & (1<<e)) {
					j++;
					continue;
				}
				// see if we can actually get from s U {e} to s -- if the key for e is available
				int t = type[e + 1];
				int sum = keycnt[0][t];
				for (int i = 0; i < N; i++) {
					if (e != i && !(s & (1<<i))) {
						// things removed from s U {e} already
						sum += keycnt[i + 1][t];
						if (type[i + 1] == t)
							sum--;
					}
				}
				if (sum <= 0)
					continue;
				//cout << " e = " << e << "; p[s | (1<<e)] = " << p[s | (1<<e)] << endl;
				// 'e' is an element we can remove from s U {e} to get s
				if (p[s | (1<<e)] < mp) {
					mp = p[s | (1<<e)];
					mj = j;
				}
			}
			if (mp != (ULL)-1) {
				p[s] = mp + (mj) * factorial[r];
				//cout << "p[" << s << "] = " << p[s] << endl;
			} else
				p[s] = mp;
		}
}

string p2str(ULL code) {
	//cout << "entering p2str()" << endl;
	int a[25];
	bool used[25];
	for (int i = 1; i <= N; i++)
		used[i] = false;
	for (int i = 1; i <= N; i++) {
		int j = code / factorial[N - i];
		int cnt = 0;
		for (int k = 1; k <= N; k++) if (!used[k]) {
			if (cnt == j) {
				a[i] = k;
				used[k] = true;
				break;
			}
			cnt++;
		}
		code = code % factorial[N - i];
	}
	stringstream ss;
	ss << a[1];
	for (int i = 2; i <= N; i++)
		ss << " " << a[i];
	return ss.str();
}

int main() {
	int ncases, tmp, tmpcnt;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> K >> N;
		reset_vars();
		for (int k = 0; k < K; k++) {
			cin >> tmp;
			keycnt[0][tmp]++;
		}
		for (int i = 1; i <= N; i++) {
			cin >> type[i] >> tmpcnt;
			for (int k = 0; k < tmpcnt; k++) {
				cin >> tmp;
				keycnt[i][tmp]++;
			}
		}
		compute_result();
		string res;
		if (p[0] == (ULL)-1)
			res = "IMPOSSIBLE";
		else
			res = p2str(p[0]);
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
