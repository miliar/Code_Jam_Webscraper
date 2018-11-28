#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <utility>
using namespace std;

int a,b,k,ans;

int main() {
	int tst;
	cin >> tst;
	for(int t=1;t<=tst;++t) {
		ans=0;
		cout << "Case #" << t << ": ";
		cin >> a >> b >> k;
		for(int i=0;i<a;++i) {
			for(int j=0;j<b;++j) {
				if((i&j) < k) ++ans;
			}
		}
		cout << ans << "\n";
	}
	return 0;
}
