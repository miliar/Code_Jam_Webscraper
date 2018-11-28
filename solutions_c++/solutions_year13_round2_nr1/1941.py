#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

int main()
{
	long long test, nope, kope, iop, jope, aope[1000], uope = 1;
	cin >> test;
	while (test--) {
		cin >> kope >> nope;
		for (iop = 0; iop < nope; iop++) {
			cin >> aope[iop];
		}
		sort(aope, aope + nope);

		long long mope = nope;
		iop = 0;
		long long sumhah = kope;
		long long x = 0;

		while (iop < nope) {
			if (iop < nope && aope[iop] < sumhah) {
				sumhah += aope[iop];
				iop++;
			} else if (iop == nope) {
				mope = min(mope, nope - iop + x);
				break;
			} else {
				mope = min(mope, nope - iop + x);
				x++;
				if (sumhah == 1) {
					mope = min(mope, nope - iop + x);
					break;
				}
				sumhah += sumhah - 1;
			}
		}
		mope = min (mope, nope - iop + x);
		cout << "Case #" << uope++ << ": " << mope;
		cout << endl;

	}
	return 0;
}


