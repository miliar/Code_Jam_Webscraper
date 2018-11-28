#include <bits/stdc++.h>
using namespace std;
#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define endl "\n"
#define sync ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define clean(a) memset((a),0,sizeof (a))
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
typedef pair<int,int> pii;
typedef long long ll;
const int N = 200005;
const int MAX = 1000000007;
const double EPS = 0.000001;
//cout << fixed << setprecision(10);

ll n,d,now;
char c[11];
int k,numb;

int main() {
	fin("A-large.in");
	fout("A.out");
	sync;
	int t;
	cin >> t;
	for(int q = 1;q<=t;q++) {
		cin >> n;
		if (!n) {
			cout << "Case #" << q << ": INSOMNIA" << endl;
			continue;
		}
		memset(c, 0, sizeof(c));
		k = 0;
		d = (ll)0;
		while(k != 10) {
			d += n;
			now = d;
			while(now && k != 10) {
				numb = now % (ll)10;
				if (!c[numb]) {
					k++;
					c[numb] = 1;
				}
				now /= (ll)10;
			}
		}
		cout << "Case #" << q << ": " << d << endl;
	}

	return 0;
}
