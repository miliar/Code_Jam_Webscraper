#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#pragma warning(disable : 4996)

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T, R, C, W, res;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cin >> R >> C >> W;
		if(W == 1) res = C;
		else {
			res = floor(C / (W));
			res += W;
			if(C % W == 0)
				--res;
		}
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}