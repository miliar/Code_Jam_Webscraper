#include <iostream>
#include <cstdio>
using namespace std;
int main() {
	freopen("inp3.txt","r",stdin);
	freopen("oup.txt","w",stdout);
	int t;
	cin >> t;
	for (int j = 1; j <= t; j++) {
		int smax;
		cin >> smax;
		char s[smax+1];
		cin >> s;
		long long sum = 0,ans = 0;
		for (int i = 0; s[i] != '\0'; i++) {
			int z = (int) s[i] - 48;
			if (i > sum) {
				ans = ans + (i-sum);
				sum = i;
			} 
			sum = sum + z;
		}
		cout << "Case #" << j << ':' << ' ' << ans << endl;
		//printf("Case #%lld: %lld\n",j,ans);
	}
	return 0;
}
