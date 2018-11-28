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
		uint64_t P, Q, I;
		char c;
		cin >> P >> c >> Q;
		while (P > (Q>>1) && Q&1 == 0) {
			P -= (Q>>1);
			Q >>= 1;
		}
		while (P&1 == 0 && Q&1 == 0) {
			P >>= 1;
			Q >>= 1;
		}
		I = (uint64_t)1 << 40;
		while (I&1 == 0 && Q&1 == 0) {
			I >>= 1;
			Q >>= 1;
		}
		I *= P;
		if (I%Q == 0) {
			I /= Q;
			int gens = 40;
			while (I > 1) {
				I >>= 1;
				gens--;
			}
			//while (Q > 1) {
			//	Q >>= 1;
			//	gens++;
			//}
			cout << "Case #" << (casei+1) << ": " << gens << endl;
		} else {
			cout << "Case #" << (casei+1) << ": impossible" << endl;
		}
	}
	return 0;
}
