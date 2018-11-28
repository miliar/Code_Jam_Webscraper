#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LL;

int main()
{
	LL base[31];

	for (int i=0; i<31; i++) {
		base[i] = 1<<i;
	}
	int T;
	
	freopen("C:\\Users\\flex\\Desktop\\B--small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\flex\\Desktop\\B-small-practice.out", "w", stdout);
	cin >> T;

	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";

		LL A, B, K;

		cin >> A >> B >> K;

		LL result  = 0;

		for (int i=0; i<A; i++) {
			for (int j=0; j<B; j++) {
					LL a = i&j;
					if (a < K) {
						result ++;
				}
			}
		}

		cout << result << endl;
	}

	return 0;
}