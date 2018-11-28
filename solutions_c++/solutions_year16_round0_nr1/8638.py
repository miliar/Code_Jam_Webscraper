#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define X first
#define Y second
#define Sz size()
#define mp make_pair
#define foreach(i, x) for(__typeof((x).begin()) i = (x).begin(); i != (x).end(); i ++)
#define Say(x) cerr << #x << " = " << x << endl
#define For(i, n) for(int i = 0; i < (n); i++)
#define ALL(x) (x).begin(), (x).end()
typedef long long ll;
typedef vector <int> vint;
typedef pair <int,int> pii;

const int M = 100 + 4, Inf = 1e9 + 10;

/////////////////////////////////////////////////////////////////////////

int main()
{
	ios::sync_with_stdio(0);
	int t, n;
	cin >> t;
	for (int i = 0; i < t; i ++) {
		cin >> n;
		if (!n) {
			cout << "Case #" << i + 1 << ": INSOMNIA\n";
			continue;
		}
		ll mark = 0, cur = n;
		while(mark != ((1ll << 10) - 1)) {
			ll tmp = cur;
			while (tmp > 0) {
				mark |= (1ll << tmp % 10);
				tmp /= 10;
			}
			cur += n;
		}
		cout << "Case #" << i + 1 << ": " << cur - n << endl;
	}
	return 0;
}
