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

const int MAXN = 1000;

int N, K;
double P[MAXN], ch[MAXN], nch[MAXN];

void run() {
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> P[i];
	}
	sort(P, P + N);
	double ans = 0.0;

//	vector<int> bestP;
//	for (int i = 0; i < (1 << N); i++) {
//		vector<double> probs;
//		vector<int> nums;
//        for (int j = 0; j < N; j++) {
//			if ((i >> j) & 1) {
//				// add j
//				probs.push_back(P[j]);
//				nums.push_back(j);
//			}
//        }
//		if (probs.size() != K) continue;
//
//		fill_n(ch, MAXN, 0.0);
//
//		ch[0] = 1.0;
//		for (double d : probs) {
////			cerr << d << ", ";
//			fill_n(nch, MAXN, 0.0);
//			for (int from = 0; from <= K; from++) {
//				if (from < K) {
//					nch[from + 1] += ch[from] * d;
//				}
//				nch[from] += ch[from] * (1 - d);
//			}
//			for (int f = 0; f <= K; f++) {
//				ch[f] = nch[f];
//			}
//		}
////		cerr << endl;
//
//		if (ans < ch[K / 2]) {
//			bestP.clear();
//			for (int j : nums) {
//				bestP.push_back(j);
//			}
//		}
//		ans = max(ans, ch[K / 2]);
//	}
//
//	// sort(bestP.begin(), bestP.end());
//	for (int j : bestP) {
//		cout << j << " ";
//	}
//	cout << endl;

	for (int tl = 0; tl <= K; tl++) {
		int tr = K - tl;

		vector<double> probs;
		for (int i = 0; i < tl; i++) {
			probs.push_back(P[i]);
		}
		for (int i = tr; i > 0; i--) {
			probs.push_back(P[N - i]);
		}

		fill_n(ch, MAXN, 0.0);
		ch[0] = 1.0;
		for (double d : probs) {
			fill_n(nch, MAXN, 0.0);
			for (int from = 0; from <= K; from++) {
				if (from < K) {
					nch[from + 1] += ch[from] * d;
				}
				nch[from] += ch[from] * (1 - d);
			}
			for (int f = 0; f <= K; f++) {
				ch[f] = nch[f];
			}
		}
		ans = max(ans, ch[K / 2]);
	}
	cout << ans << endl;
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
		cout << "Case #" << tc << ": ";
		run();
	}

	return 0;
}
