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
const int N = 35;
const int MAX = 1000000007;
const double EPS = 0.000001;
//cout << fixed << setprecision(10);

int n;
int a[N];
int main() {
	fin("A.in");
	fout("A.out");
	sync;
	int t;
	cin >> t;
	int ma,maxi;
	for(int q = 0;q<t;q++) {
		cin >> n;
		for(int i = 0;i<n;i++)
			cin >> a[i];
		bool f = true;
		cout << "Case #" << q+1 << ": ";
		if (n == 2) {
			if (a[0] > a[1])
				maxi = 0;
				else maxi = 1;
			while(a[0] != a[1]) {
				cout << (char)('A'+maxi) << " ";
				a[maxi]--;
			}
			while(a[0]) {
				cout << "AB ";
				a[0]--;
				a[1]--;
			}
			cout << endl;
			continue;
		}
		while(f) {
			f = false;
			ma = -1;
			maxi = -1;
			for(int i = 0;i<n;i++)
				if (a[i]!=1 && a[i] > ma) {
					ma = a[i];
					maxi = i;
				}
			if (ma != -1) {
				f = true;
				cout << (char)('A' + maxi) << " ";
				a[maxi]--;
			}
		}
		int cnt = n;
		int i = 0;
		while(cnt != 2) {
			cout << (char)('A'+i) << " ";
			i++;
			cnt--;
		}
		cout << (char)('A'+n-2) << (char)('A'+n-1);
		cout << endl;
	}
	return 0;
}
