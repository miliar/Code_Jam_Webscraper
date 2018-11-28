#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
	freopen("output.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	int T;
	cin >> T;
	int n;
	int current;
	bool appear[10];
	int k;
	for (int t=1; t<=T; t++) {
		cin >> n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		for (int i=0; i<10; i++)
			appear[i] = false;
		k = 1;
		while (true) { // < 100
			current = k * n;
			while (current > 0) {
				appear[current%10] = true;
				current /= 10;
			}
			bool done = true;
			for (int i=0; i<10; i++) {
				if (!appear[i]) {
					done = false;
					break;
				}
			}
			if (done) {
				printf("Case #%d: %d\n", t, k*n);
				break;
			}else {
				k += 1;
			}
		}
	}
	return 0;
}