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

int a[100][100];

int sumX[100], sumY[100];
int N, M;
int rX[100], rY[100];

bool check() {
	REP(i, 100) {
		rX[i] = rY[i] = 0;
	}
	for(int p = 101; p > 0; p--) {
		REP(i, N) {
			REP(j, M) {
				if (a[i][j] == p) {
					if (rX[i] > p && rY[j] > p) {
						return false;
					} else {
						rX[i] = max(p, rX[i]);
						rY[j] = max(p, rY[j]);
					}
				}
			}
		}
	}
	return true;
}


int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	REP(k, T) {
		cout << "Case #" << (k+1) << ": ";
		cin >> N >> M;
		REP(i, N) {
			REP(j, M) {
				cin >> a[i][j];
				sumX[i] += a[i][j];
				sumY[j] += a[i][j];
			}
		}
		cout << (check() ? "YES" : "NO") << endl;
	}
	
    return 0;
}