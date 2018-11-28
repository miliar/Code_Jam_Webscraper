#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;


int main() {
	int t, n, i, count, p, m, times, aux;
	
	scanf("%d", &t);
	p = 1;
	while (t--) {
		vector<bool> seen(10, false);
		scanf("%d", &n);
		times = 1;
		if (n == 0) {
			cout << "Case #" << p << ": INSOMNIA" << endl;
			p++;
			continue;
		}
		while (true) {
			m = times * n;
			aux = m;
			while (m != 0) {
				seen[m % 10] = true;
				m = m / 10;
			}
			count = 0;
			for (i = 0; i < 10; i++) {
				if (seen[i])
					count++;
			}
			if (count == 10) {
				cout << "Case #" << p << ": " << aux << endl;
				p++;
				break;
			}
			times++;
		}
	}
	
	return 0;
}
