#include<bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

ostream& operator<<(ostream &out, const pii &a) { return out << '(' << a.first << ", " << a.second << ')'; }
istream& operator>>(istream &in, pii &a) { return in >> a.first >> a.second; }

const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

// lambda-expression: [] (args) -> retType { body }

const int maxn = 12;
const int maxm = 1 << maxn;
const int sz = maxm * 2;

int N, M, P, R, S;

//int nr[sz];

string fill_down(int i, int c)
{
	if (i >= M) {
		switch (c) {
			case 0: return "P";
			case 1: return "R";
			case 2: return "S";
		}
		return "";
		// return "PRS"[(int) c];
	} else {
		int d =(c + 1) % 3;
		string l = fill_down(2 * i, c);
		string r = fill_down(2 * i + 1, d);
		if (l < r) {
			return l + r;
		} else {
			return r + l;
		}
	}
}

int cnt[256] = {};

void run(int tc) {
	cin >> N >> R >> P >> S;
	M = 1 << N;

//	int ns = -1;
	bool hasAns = false;
	string result = "Z";

	for (int s = 0; s < 3; s++) {
		string ans = fill_down(1, s);
//		cerr << s << ": " << ans << endl;

		fill_n(cnt, 256, 0);
		for (char c : ans) {
			cnt[(int) c]++;
		}

//		cerr << cnt['P'] << " " << cnt['R'] << " " << cnt['S'] << endl;

		if (cnt['P'] == P && cnt['R'] == R && cnt['S'] == S) {
//			cerr << "CHECK " << result <<" " << ans << endl;
			result = min(result, ans);
			hasAns = true;
		}

//		nr[1] = s;
//		for (int i = 1; i < M; i++) {
//			nr[2 * i] = nr[i];
//			nr[2 * i + 1] = (nr[i] + 1) % 3;
//			if (nr[2 * i + 1] < nr[2 * i]) {
//				swap(nr[2 * i], nr[2 * i + 1]);
//			}
//		}
//
//		int cnt[3] = {};
//		for (int i = 0; i < M; i++) {
//			cnt[nr[M + i]]++;
//		}
//
//		if (cnt[0] == P && cnt[1] == R && cnt[2] == S) {
//			ns = s;
//			break;
//		}
	}

	cout << "Case #" << tc << ": ";
	if (hasAns) {
		cout << result << endl;
	} else {
		cout << "Impossible" << endl;
	}
}

int main() {
#ifdef LOCAL
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
#endif // LOCAL
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// cerr << boolalpha;
	(cout << fixed).precision(10);

	int ntc;
	cin >> ntc;
	for (int tc = 1; tc <= ntc; tc++) {
		run(tc);
	}

	return 0;
}
