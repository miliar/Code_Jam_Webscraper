#include <bits/stdc++.h>

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

struct pt
{
	int x, y, z;
};

istream& operator>>(istream &in, pt &p)
{
	return in >> p.x >> p.y >> p.z;
}

const int MAXN = 1000;

int n, s;
pt loc[MAXN], vel[MAXN];

int maxdist[MAXN];

int dist(int i, int j)
{
	return (loc[i].x - loc[j].x) * (loc[i].x - loc[j].x) + (loc[i].y - loc[j].y) * (loc[i].y - loc[j].y) + (loc[i].z - loc[j].z) * (loc[i].z - loc[j].z);
}

void run(int tc)
{
	cin >> n >> s;
	for (int i = 0; i < n; i++) {
		cin >> loc[i] >> vel[i];
	}

	fill_n(maxdist, MAXN, INF);
	maxdist[0] = 0;

	set<pii> q;
	q.insert(pii(maxdist[0], 0));
	while (!q.empty()) {
		int d = q.begin()->first;
		int cur = q.begin()->second;
		q.erase(q.begin());
		for (int i = 0; i < n; i++) {
			int alt = max(d, dist(cur, i));

//			cerr << cur << " -> " << i << ": " << alt << endl;

			if (alt < maxdist[i]) {
				q.erase(pii(maxdist[i], i));
				maxdist[i] = alt;
				q.insert(pii(maxdist[i], i));
			}
		}
	}

	int answer = maxdist[1];

	double answerD = sqrt(1.0 * answer);

	cout << "Case #" << tc << ": " << answerD << endl;
}

int main()
{
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
