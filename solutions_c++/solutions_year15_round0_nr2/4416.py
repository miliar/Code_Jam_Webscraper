#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAXN = 1009;
int cs, n;
int a[MAXN], b[MAXN];

int main() {
//	ifstream cin ("txt.in");
//	ofstream cout ("txt1.out");
	cin >> cs;
	for (int T = 1; T <= cs; T++) {
		cin >> n;
		memset (a, 0, sizeof a);
		for (int i = 1, x; i <= n; i++) {
			cin >> x;
			a[x]++;
		}
		int ans = 0x7fffffff;
		for (int i = 1000; i > 0; i--) {
			int tem = i;
			memcpy (b, a, 10 * sizeof (int) );
			for (int j = 1000; j > i; j--) {
				for (int k = j; k > i && b[k] > 0; k -= i) {
					tem += b[k];
					b[k - i] += b[k];
					b[k]=0;
				}
			}
			ans = min (ans, tem);
		}
		cout << "Case #" << T << ": " << ans << endl;
	}
}
