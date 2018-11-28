#include <iostream>
#include <cstdio>
#include <vector>;

using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("/Users/malzantot/Documents/codingspace/A-large.in.txt", "r", stdin);
	 freopen("/Users/malzantot/Documents/codingspace/A-large-out.txt", "w", stdout);

#endif
	
	int tt;
	cin >> tt;
	for (int it = 1; it <= tt; it++) {
		unsigned long long n;
		cin>> n;
		int mem = 0;
		unsigned long long x = n;
		unsigned long long i = 1;

		bool insomnia = false;
		while(true) {
			x = (i++) * n;
			if (x==0) {
				insomnia = true;
				break;
			}
			int tmp = x;
			while (tmp > 0) {
				int d = tmp%10;
				tmp = tmp/10;
				mem |= (1<<d);
			}
			if (mem == 1023)
			break;

		}

		if (insomnia) {
			printf("Case #%d: INSOMNIA\n", it);

		} else {
		printf("Case #%d: %d\n", it, x);
		}

	}

	return 0;

}
