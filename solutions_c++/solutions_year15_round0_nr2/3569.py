#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

int d;
int cake[1010];

int main() {
	int t;
	cin >> t;

	for (int cs = 1; cs <= t; ++cs) {
		int lim = 0, sol, temp;
		memset(cake, 0, sizeof(cake));
		
		cin >> d;
		for (int i = 0; i < d; ++i) {
			cin >> cake[i];
			lim = max(lim, cake[i]);
		}

		sol = lim;
		for (int i = 1; i <= lim; ++i) {
			temp = i;
			for (int j = 0; j < d; ++j) {
				if (cake[j] <= i)
					continue;
				temp += (cake[j] / i) + (cake[j] % i == 0 ? -1 : 0); 
			}
			sol = min(sol, temp);
		}

		cout << "Case #" << cs << ": " << sol << endl;
	}

	return 0;
}
