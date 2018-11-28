#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

int getV(int n) {
	int u = 0;
	while (n) {
		u |= 1 << n % 10;
		n /= 10;
	}
	return u;
}

int main() {
	int T, N, caso=1;
	cin >> T;
	while (T--) {
		cin >> N;
		cout << "Case #" << caso++ << ": ";
		int u = getV(N), cN = N;
		while (u != (1 << 10) - 1) {
			cN += N;
			u |= getV(cN);
			if (!cN) break;
		}
		if(cN) cout << cN << endl;
		else cout << "INSOMNIA" << endl;
	}
	return 0;
}
