#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int l, L = 0;
	cin>>l;
	while (L++ < l) {
		cout<<"Case #"<<L<<": ";
		int s, tot = 0, ans = 0;
		cin>>s;
		int a[1001];
		for (int i = 0; i <= s; ++i) {
			char c;
			cin>>c;
			a[i] = c - '0';
			if (tot < i) {
				ans = max(ans, i - tot);
			}
			tot += a[i];
		}
		cout<<ans<<endl;
	}
}
