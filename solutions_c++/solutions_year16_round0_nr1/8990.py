/* [theMighty] Deathsurgeon (Rupesh Maity)
* 3rd year, B.Tech in IT
* IIIT Allahabad
*/

#define _CRT_SECURE_NO_WARNINGS

#include <bits/stdc++.h>

#define ll long long
#define pii pair<int, int>

#define MOD 1000000007
#define MAX 100001
#define sd(x) scanf("%d", &x)

using namespace std;

int main()
{
#ifdef _MSC_VER
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		int n;
		cin >> n;

		bool done[10] = {};

		for (int i = 1; i < 1000; i++) {
			int p = n * i;

			while (p) {
				done[p % 10] = true;
				p /= 10;
			}

			bool b = true;
			for (int j = 0; j < 10; j++) {
				if (!done[j])
					b = false;
			}

			if (b) {
				cout << i * n << endl;
				goto DONE;
			}
		}

		puts("INSOMNIA");
	DONE:;
	}



	return 0;
}