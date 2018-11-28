#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define L(a) (int)((a).size())
#define all(a) (a).begin(), (a).end()
#define mp make_pair

#define Trace(X) cerr << #X << " = " << X << endl
#define _ << " - " << 

void mark(ll n, int &mask) {
	while (n > 0) {
		mask |= 1 << (n%10);
		n /= 10;
	}
}

int main() {
	ios_base::sync_with_stdio(0);cin.tie(0);
	
	int TC;
	cin >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		ll n;
		cin >> n;

		cout << "Case #" << tc << ": ";
		if (n == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			int mask = 0;
			ll startN = n;
			do {
				mark(n, mask);
				n += startN;
			} while (mask != (1 << 10) - 1);
			cout << n - startN << endl;
		}
	}
    return 0;
}









