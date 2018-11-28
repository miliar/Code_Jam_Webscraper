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
#define mp make_pair
#define pb push_back

typedef long double dbl;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const dbl pi = 3.14159265358979323846;
const int inf = (int) 1e9;
const dbl eps = 1e-9;

vector<LL> st[15];
int out[9];

void pre() {
	REPE(i,2,10) {
		LL v = 1;
		FOR(j,18) {
			st[i].pb(v);
			v *= i; 
		}
	}
}

VI go(int v, int n) {
	VI res;
	if (v == 0) {
		res.pb(0);
	}
	while(v) {
		res.pb(v % 2);
		v /= 2;
	}
	while((int)res.size() < n) {
		res.pb(0);
	}
	//reverse(res.begin(), res.end());
	return res;
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
#endif
	int tmp;
	cin >> tmp;
	int n,j;
	cin >> n >> j;
	pre();
	cout << "Case #1:";
	int all = 0;
	for(int i = 1; i < 1 << n; i += 2) {
		VI now = go(i, n - 1);
		bool add = true;
		REPE(k,2,10) {
			LL val = st[k][n - 1];
			FOR(l,now.size()) {
				if (now[l]) {
					val += st[k][l];
				}
			}
			LL sq = sqrt(val +.0);
			LL check = 0;
			REPE(l,2,sq) {
				if (val % l == 0) {
					check = l;
					break;
				}
			}
			if (check == 0) {
				add = false;
				break;
			}
			out[k - 2] = check;
		}
		if (add) {
			cout << "\n1";
			reverse(now.begin(), now.end());
			FOR(l,now.size()) {
				cout << now[l];
			}
			FOR(l,9) {
				cout << " " << out[l];
			}
			++all;
		}
		if (all == j) {
			break;
		}
	}
    return 0;
}