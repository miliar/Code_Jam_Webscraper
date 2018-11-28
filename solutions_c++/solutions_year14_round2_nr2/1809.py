#include <assert.h>
#include <cstring>
#include <iostream>
using namespace std;

int A, B, K;

void deal()
{
	int ans = 0;
	cin >> A >> B >> K;
	for (int i = 0; i < A; ++i) {
		for (int j = 0; j < B; ++j) {
			if ((i & j) < K) {
				//cerr << i << ' ' << j << endl;
				++ans;
			}
		}
	}
	cout << ans << endl;
}

int main()
{
	int cases;
	ios::sync_with_stdio(false);
	cin >> cases;
	for (int t = 1; t <= cases; ++t) {
		cout << "Case #" << t << ": ";
		deal();
	}

	return 0;
}
