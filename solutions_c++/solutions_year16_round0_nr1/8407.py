#include <bits/stdc++.h>

using namespace std;

int getn () {
	int n;
	scanf("%d", &n);
	return n;
}

int main () {
	int N = getn();
	for (int i = 0; i < N; ++i) {
		int q = getn();
		bitset<10> was;
		long long c = 0;
		if (!q) printf("Case #%d: INSOMNIA\n", i+1);
		else {
			while (!was.all()) {
				c++;
				string s = to_string(q*c);
				for (int j=0; j<s.size(); j++) {
					was[s[j] - '0'] = 1;
			//		cout << was << endl;
				}
				
			}	
			printf("Case #%d: %lld\n", i+1, c*q);
		}
	}
	

}