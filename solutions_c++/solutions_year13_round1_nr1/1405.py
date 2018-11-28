#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

int main() {

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	int T;
	long long r, t;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> r >> t;
		long long n = 1, count = 0;
		
		while (t > 0) {
			t = t - (2*r + 2*n - 1);
			if (t >= 0) {
				count++;
				n += 2;
			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}