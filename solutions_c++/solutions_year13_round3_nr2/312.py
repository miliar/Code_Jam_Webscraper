#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue> 
#include <algorithm>
#include <bitset>
#include <set>

using namespace std;

#define REP(i,n) for(long long int i = 0; i < int(n); ++i)
#define REPV(i, n) for (long long int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(long long int i = (int)(a); i < (int)(b); ++i)

#define ALL(v) (v).begin(), (v).end()
#define PF push_front
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define lli long long int

int x;
int yy;

char str[1000];

bool f(int kx, int ky, int inc) {
	if (kx == x && ky == yy) return true;
	if (inc > 200) return false;
	int dX = x - kx;
	int dY = yy - ky;
	if (dX > dY) {
		if (dX > 0) {
			if (f(kx + inc, ky, inc + 1)) {
				str[inc] = 'E';
				return true;
			}
			if (f(kx - inc, ky, inc + 1)) {
				str[inc] = 'W';
				return true;
			}
			if (f(kx, ky + inc, inc + 1)) {
				str[inc] = 'N';
				return true;
			}
			if (f(kx, ky - inc, inc + 1)) {
				str[inc] = 'S';
				return true;
			}
		} else {
			if (f(kx - inc, ky, inc + 1)) {
				str[inc] = 'W';
				return true;
			}
			if (f(kx + inc, ky, inc + 1)) {
				str[inc] = 'E';
				return true;
			}
			if (f(kx, ky + inc, inc + 1)) {
				str[inc] = 'N';
				return true;
			}
			if (f(kx, ky - inc, inc + 1)) {
				str[inc] = 'S';
				return true;
			}
		}
	} else {
		if (dY > 0) {
			if (f(kx, ky + inc, inc + 1)) {
				str[inc] = 'N';
				return true;
			}
			if (f(kx, ky - inc, inc + 1)) {
				str[inc] = 'S';
				return true;
			}
			if (f(kx + inc, ky, inc + 1)) {
				str[inc] = 'E';
				return true;
			}
			if (f(kx - inc, ky, inc + 1)) {
				str[inc] = 'W';
				return true;
			}			
		} else {
			if (f(kx, ky - inc, inc + 1)) {
				str[inc] = 'S';
				return true;
			}
			if (f(kx, ky + inc, inc + 1)) {
				str[inc] = 'N';
				return true;
			}
			if (f(kx + inc, ky, inc + 1)) {
				str[inc] = 'E';
				return true;
			}
			if (f(kx - inc, ky, inc + 1)) {
				str[inc] = 'W';
				return true;
			}	
		}
	}
	return false;
}



int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif	
	int T;
	cin >> T;
	REP(q, T) {
		cin >> x >> yy;
		cout << "Case #" << (q + 1) << ": ";
		
		for(int i = 0; i < abs(yy); ++i) {
			cout << ((yy > 0) ? "SN" : "NS");
		}
		for(int i = 0; i < abs(x); ++i) {
			cout << ((x > 0) ? "WE" : "EW");
		}
		cout << endl;
	}
    return 0;
}