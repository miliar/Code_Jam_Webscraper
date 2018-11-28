#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int caseNo = 1;
int T, n, i, warWins, dwarWins, pos_a, pos_b;
double aux;
typedef long long ll;
vector<ll> a, b;

void playWar() {
	pos_a = pos_b = 0;
	for (i = 0; i < n; ++i) {
		for (; unsigned(pos_b) < b.size(); ++pos_b) {
			if (b[pos_b] > a[pos_a]) {
				warWins++;
				++pos_b;
				break;
			}
		}
		++pos_a;
	}
}

void playDWar() {
	int lim_inf = 0;// , lim_sup = n - 1;
	for (i = 0; i < n; ++i) {
		if (a[i] < b[lim_inf]) {
			dwarWins++;
//			--lim_sup;
		}
		else {
			++lim_inf;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	while (T--) {
		warWins = dwarWins = 0;
		a.clear();
		b.clear();
		cin >> n;
		for (i = 0; i < n; ++i) {
			cin >> aux;
			aux *= double(100000);
			a.push_back(ll(aux));
		}
		for (i = 0; i < n; ++i) {
			cin >> aux;
			aux *= double(100000);
			b.push_back(ll(aux));
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		playWar();
		playDWar();
		cout << "Case #" << caseNo++ << ": " << n - dwarWins << " " << n - warWins << endl;
	}
	return 0;
}