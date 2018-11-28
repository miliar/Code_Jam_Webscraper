#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vb> vvb;
typedef vector<vs> vvs;
typedef vector<vl> vvl;

int inf = 0x3f3f3f3f;
double eps = 10e-10;
ll mod = 1000000007ll;

#define rep(k, a, b) for (int k = (a); k < int(b); k++)
#define sz(a) int(a.size())
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define x first
#define y second
#define mi(r, c, v) vvi(r, vi(c, v))
#define rrep(k, a, b) for (int k = (a); k >= int(b); k--)
#define irep(k, a) for (auto& k : (a))
#define md(r, c, v) vvd(r, vd(c, v))
#define mb(r, c, v) vvb(r, vb(c, v))
#define ms(r, c, v) vvs(r, vs(c, v))
#define ml(r, c, v) vvl(r, vl(c, v))
#define mc(r, c, v) vs(r, string(c, v))
#define add(i, j) ((i) + (j)) % mod
#define mul(i, j) ((i) * (j)) % mod
#define bits(n) int(__builtin_popcount(n))

// test include_empty = true, test tokenFunc
vs tokenizer(const string& s, int(tokenFunc)(int) = isspace, bool include_empty = false) {
	vs result;
	int front = 0;
	rep(i, 0, sz(s) + 1) {
		if (i == sz(s) || tokenFunc(s[i])) {
			if (include_empty || i != front)
				result.pb(s.substr(front, i - front));
			front = i + 1;
		}
	}
	return result;
}

template<class T>
class Index {
	unordered_map<T, int> index;
	vector<T> label;
public:
	inline T getL(int ind) const { return label[ind]; }
	inline int size() const { return sz(label); }
	inline int getI(const T& e) {
		if (index.find(e) == index.end()) {
			int t = sz(index);
			index[e] = t;
			label.pb(e);
		}
		return index[e];
	}
};

int main() {
	int T, n;
	cin >> T;
	rep(X, 0, T) {
		cin >> n;
		vvi nums(n);
		int ans = inf;
		string s;
		Index<string> ind;
		getline(cin, s);

		rep(i, 0, n) {
			getline(cin, s);
			vs tokens = tokenizer(s);
			irep(t, tokens)
				nums[i].pb(ind.getI(t));
		}

		rep(k, 0, 1 << (n - 2)) {
			vi common(sz(ind));
			int curans = 0;
			irep(x, nums[0])
				common[x] |= 1;
			irep(x, nums[1])
				common[x] |= 2;
			rep(i, 0, n - 2) {
				if ((k & (1 << i)) == 0) {
					irep(x, nums[i + 2])
						common[x] |= 1;
				} else {
					irep(x, nums[i + 2])
						common[x] |= 2;
				}
			}

			irep(v, common) {
				if (v == 3)
					curans++;
			}
			ans = min(ans, curans);
		}

		printf("Case #%d: %d\n", X + 1, ans);
	}
}
