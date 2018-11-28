#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define sz(v) int(v.size())
#define endl '\n'
typedef long long ll;
typedef pair<int,int> pii;

const int MAXn = 1e4+10;
int a[MAXn];

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int n, x;
		cin >> n >> x;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a+n);
		int l = 0;
		int c = 0;
		for(int i = n-1; i >= l; i--) {
			if(i > l && a[i] + a[l] <= x)
				l++;
			c++;
		}
		cout << "Case #" << t << ": " << c << endl;
	}
	return 0;
}
