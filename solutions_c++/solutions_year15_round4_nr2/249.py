#include <iostream>
#include <iomanip>
#include <algorithm>
#include "stdio.h"

using namespace std;

struct pine {
	double r;
	double c;
	double rl;
};

bool operator<(const pine &x, const pine &y)
{
    return x.c < y.c;
}

int main() {
	int t;
	cin >> t;

	int n;
	double v, x;
	
	pine p[128];
	//pine p[5];

	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> n >> v >> x;

		for (int i = 0; i < n; ++i) {
			cin >> p[i].r >> p[i].c;
			p[i].rl = p[i].r;
		}

		sort(p, p+n);

		int ptl;
		for (ptl = 0; ptl < n; ++ptl) {
			if (p[ptl].c + 1e-6 < x)
				continue;
			else
				break;
		}

		int ptr;
		for (ptr = n-1; ptr >= 0; --ptr) {
			if (p[ptr].c - 1e-6 > x)
				continue;
			else
				break;
		}
		
		if (ptl >= n || ptr < 0)
			goto fail;

		double speed = 0;
		for (int i = ptl; i <= ptr; ++i) {
			speed += p[i].r;
			p[i].rl = 0;
		}

		ptl --;
		ptr ++;

		while (ptl >= 0 && ptr < n) {
			double left = (x-p[ptl].c) * p[ptl].rl;
			double right = (p[ptr].c - x) * p[ptr].rl;

			double thisRate = 0;
			if (left > right*(1 + 1e-6)) {
				//right to full
				thisRate += p[ptr].rl;
				thisRate += right / (x-p[ptl].c);
				p[ptl].rl -= right / (x-p[ptl].c);

				ptr ++;
			}
			else if (left*(1 + 1e-6) < right) {
				//left to full
				thisRate += p[ptl].rl;
				thisRate += left / (p[ptr].c - x);
				p[ptr].rl -= left / (p[ptr].c - x);

				ptl --;
			}
			else {
				// all to full
				thisRate += p[ptl].rl;
				p[ptl].rl = 0;
				thisRate += p[ptr].rl;
				p[ptr].rl = 0;

				ptl --;
				ptr ++;
			}

			speed += thisRate;
		}
		
		double timecost = v / speed;

		cout << "Case #" << tcount << ": ";
		cout << setiosflags(ios::fixed) << setprecision(9) << timecost << endl;
		continue;
fail:
		cout << "Case #" << tcount << ": IMPOSSIBLE" << endl;

	}

	return 0;
}