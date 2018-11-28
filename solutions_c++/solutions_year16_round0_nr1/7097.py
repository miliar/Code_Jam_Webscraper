#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define x first
#define y second

int main()
{
	int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		ll V;
		cin >> V;
		bool imp = false;
		if (V == 0) imp = true;
		else {
			bool seen[10] = {false};
			int c = 10;
			int i;
			for (i = 1; c && i < 100000000; ++i) {
				ll x = V * i;
				while (x > 0) {
					int b = x % 10;
					x /= 10;
					if (!seen[b]) {
						c--;
						seen[b] = true;
					}
				}
			}
			if (i != 100000000)
				V *= --i;
			else
				imp = true;
		}
		printf("Case #%d: ", casen);
		if (imp)
			printf("INSOMNIA\n");
		else
			printf("%d\n", V);
	}
	
	return 0;
}

