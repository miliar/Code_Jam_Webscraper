#include<string>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>

using namespace std;

const long long mod = 1000002013;
int T;
long long n, m;
long long o[1010], e[1010], p[1010];
vector<int> vec;
vector<long long> a;
long long total_cost;

vector<int> to, te, tp;
long long best_cost;

int min(int a, int b) {
	return a < b? a: b;
}

void init() {
	vec.clear();
	a.clear();
	total_cost = best_cost = 0;
	cin >> n >> m;
	for (int i=0; i<m; ++i) {
		cin >> o[i] >> e[i] >> p[i];
		vec.push_back(o[i]);
		vec.push_back(e[i]);
		total_cost += p[i] * ((n + n - e[i] + o[i] + 1) * (e[i] - o[i]) / 2 % mod) % mod;
	}
	sort(vec.begin(), vec.end());
	vec.erase(unique(vec.begin(), vec.end()), vec.end());
	for (int i=0; i<vec.size(); ++i) a.push_back(0);
	for (int i=0; i<m; ++i)
		for (int j=0; j<vec.size(); j++)
			if (vec[j] > o[i] && vec[j] <= e[i])
				a[j] += p[i];
}

long long work() {
    to.clear(); te.clear(); tp.clear();
    for (int i=0; i<a.size() - 1; i++)
		while (a[i+1] > 0) {
			int final = 0;
			long long minp = a[i + 1];
			for (int j=i+1; j<a.size(); j++)
				if (a[j] == 0) break;
				else {
					final = j;
					minp = min(minp, a[j]);
				}

			if (final > i && minp > 0) {
				to.push_back(vec[i]);
				te.push_back(vec[final]);
				tp.push_back(minp);
				for (int j=i+1; j<=final; ++j) a[j] -= minp;
			}
		}

    for (int i=0; i<to.size(); i++) {
 	    best_cost += tp[i] * ((n + n - te[i] + to[i] + 1) * (te[i] - to[i]) / 2 % mod) % mod;
    }
    return (total_cost + mod - best_cost) % mod;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (int i=1; i<=T; i++) {
		init();
		cout << "Case #" << i << ": " << work() << endl;
	}
	return 0;
}