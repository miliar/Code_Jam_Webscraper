//      ------>>          in the name of Allah          <<------
#include <memory.h>
#include <iostream>

#define endl "\n"

using namespace std;

int main() { ios::sync_with_stdio(0); cin.tie(0);
	int T, X = 1;
	cin >> T;
	while(T--) {
		long long n;
		cin >> n;
		long long ans = 0;
		int flag = 0;
		bool a[10];
		memset(a, 0, sizeof a);
		if(n != 0) {
			while(flag < 10) {
				ans += n;
				long long t = ans;
				while(t) {
					if(a[t%10] == 0) {
						a[t%10] = 1;
						flag++;
					}
					t/=10;
				}
			}
		}
		if(ans == 0) cout << "Case #" << X++ << ": " << "INSOMNIA" << endl;
		else cout << "Case #" << X++ << ": " << ans << endl;
	}
	return 0;
}