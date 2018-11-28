#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define sz(v) int(v.size())
#define endl '\n'
typedef long long ll;
typedef pair<int,int> pii;

const int MAXn = 1005;
int n;
int a[MAXn];

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> n;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		int l = 0, r = n-1;
		int c = 0;
		while(l < r) {
			int mn = l;
			for(int i = l; i <= r; i++)
				if(a[mn] > a[i])
					mn = i;
			if(mn - l <= r - mn) {
				for(int i = mn; i > l; i--) {
					swap(a[i], a[i-1]);
					c++;
				}
				l++;
			} else {
				for(int i = mn; i < r; i++) {
					swap(a[i], a[i+1]);
					c++;
				}
				r--;
			}
		}
		cout << "Case #" << t << ": " << c << endl;
	}
	return 0;
}
