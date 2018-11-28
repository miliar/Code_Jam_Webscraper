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

const int MAXN = 25;

int N;
bool v[MAXN][MAXN];

bool /* usedP[MAXN], */ usedF[MAXN];
int perm[MAXN];

bool canReach(int idx)
{
	if (idx == N) return true;

	int user = perm[idx];
	bool any = false;
	for (int i = 0; i < N; i++) {
		if (v[user][i] && !usedF[i]) {
			any = true;
			usedF[i] = true;
			if (!canReach(idx + 1)) {
				return false;
			}
			usedF[i] = false;
		}
	}
	return any;
}

bool orderingOK()
{
//	fill_n(usedP, N, false);
	fill_n(usedF, N, false);

	// process perm in order
	return canReach(0);
}

bool isGood()
{
	for (int i = 0; i < N; i++) {
		perm[i] = i;
	}

	do {
		if (!orderingOK()) {
			return false;
		}
	} while (next_permutation(perm, perm + N));

	return true;
}

int minSolve(int i, int j, int used)
{
	if (i == N) {
		return isGood() ? used : -1;
	} else {
		int ni = i, nj = j + 1;
		if (nj == N) { ni++, nj = 0; }

		int a = minSolve(ni, nj, used);
		if (!v[i][j]) {
			v[i][j] = true;
			int b = minSolve(ni, nj, used + 1);
			v[i][j] = false;
			if (a == -1 || (a >= 0 && b >= 0 && b < a)) {
				a = b;
			}
		}

		return a;
	}
}

void run() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < N; j++) {
			v[i][j] = (s[j] == '1');
		}
	}

	cout << minSolve(0, 0, 0) << endl;
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
