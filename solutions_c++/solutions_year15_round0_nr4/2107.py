#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <bitset>
#include <iterator>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define pb push_back

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf = (int) 1e9;


int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
    //freopen("i.in","r",stdin);
    //freopen("i.out","w",stdout);
#endif
	int T;
	cin >> T;
	FOR(TT,T) {
		if (TT) {
			cout << "\n";
		}
		cout << "Case #" << TT + 1 << ": ";
		int x,r,c;
		cin >> x >> r >> c;
		if (r > c) {
			swap(r,c);
		}
		if (x == 1) {
			cout << "GABRIEL";
			continue;
		}
		if (x == 2) {
			if ((r * c) % 2 == 0) {
				cout << "GABRIEL";
			} else {
				cout << "RICHARD";
			}
			continue;
		}
		if (x == 3) {
			if (r == 1) {
				cout << "RICHARD";
			} else {
				if ((r * c) % 3 == 0) {
					cout << "GABRIEL";
				} else {
					cout << "RICHARD";
				}
			}
			continue;
		}
		if (x == 4) {
			if (r == 4 && c == 4 || r == 3 && c == 4) {
					cout << "GABRIEL";
				} else {
					cout << "RICHARD";
				}
		}
	}
    return 0;
}