#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	
	cin >> t;
	for (int ct = 1; ct <= t; ct++) {
		int a, b, k;
		int ctr = 0;
		
		cin >> a >> b >> k;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i & j) < k) {
					ctr++;
				}
			}
		}

		printf("Case #%d: %d\n", ct, ctr);
	}
	
	return 0;
}
