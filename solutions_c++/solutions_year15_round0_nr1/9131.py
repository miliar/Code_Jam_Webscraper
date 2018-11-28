#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1e-10
#define INF 1000000
#define mp make_pair
#define pb push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef long long ll;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int Smax;
		string Aud;
		cin >> Smax >> Aud;
		int sum = 0, ans = 0;
		for (int d = 0; d < Aud.size(); d++) {
			int num = int(Aud[d]-'0'),
			    diff = d - sum;
			sum += num;
			if (diff > 0) {
				sum += diff;
				ans += diff;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
