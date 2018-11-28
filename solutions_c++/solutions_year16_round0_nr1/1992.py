#include <bits/stdc++.h>

using namespace std;

bool areAllThere(string digits, vector<bool> &isThere) {
	for(auto d : digits) {
		isThere[d - '0'] = true;
	}

	for(auto x : isThere) {
		if(x == false) return false;
	}
	return true;
}

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++) {
		int N;
		scanf("%d", &N);

		vector<bool> isThere(10, false);

		int res = -1;
		if(N != 0) {
			for(int i = 1; i*N < 1000000; i++) {
				int n = i*N;
				if(areAllThere(to_string(n), isThere)) {
					res = n;
					break;
				}
			}
		}

		if(res == -1) {
			printf("Case #%d: INSOMNIA\n", t);
		}
		else {
			printf("Case #%d: %d\n", t, res);
		}

	}

	return 0;
}