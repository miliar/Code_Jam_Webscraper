#include <iostream>
#include <algorithm>
using namespace std;

int main () {
	int T;
	cin>>T;
	int t = 0;
	while (t++ < T) {
		int d, m = 0, ans = 999999999;
		int p[1001];
		cin>>d;
		for (int i = 0; i < d; ++i) {
			cin>>p[i];
			m = max(m, p[i]);
		}
		for (int i = m; i; --i) {
			int tmp = i;
			for (int j = 0; j < d; ++j) {
				int t = p[j];
				while (t > i) {
					++tmp;
					t -= i;
				}
			}
			ans = min(ans, tmp);
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
