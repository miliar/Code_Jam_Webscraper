#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define forl(i,a,b) for(int i = a; i < b; ++i)

int main()
{
	int numcases = 0;
	cin >> numcases;
	forl(casei, 0, numcases) {
		int A, B, K;
		cin >> A >> B >> K;
		if (A < K || B < K) {
			cout << "Case #" << (casei+1) << ": " << A*B << endl;
		} else {
			int total = 0;
			/*int min;
			if (A < B) min = A;
			else min = B;*/
			forl(a, 0, A) {
				forl(b, 0, B) {
					if ((int)(a&b) < K) total++;
				}
			}
			cout << "Case #" << (casei+1) << ": " << total << endl;
		}
	}
	return 0;
}
