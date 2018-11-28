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

bool t[10];

int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
#endif
	int T;
	cin >> T;
	REPE(TT,1,T) {
		if (TT != 1) {
			cout << "\n";
		}
		cout << "Case #" << TT << ": ";
		LL n;
		cin >> n;
		memset(t,false, sizeof(t));
		if (n == 0) {
			cout << "INSOMNIA";
			continue;
		}
		int cnt = 10;
		LL k = 1;
		while(cnt != 0) {
			LL now = n * k;
			while(now) {
				if (!t[now % 10]) {
					t[now % 10] = true;
					--cnt;
				}
				now /= 10;
			}
			if (!cnt) {
				break;
			}
			++k;
		}
		cout << n * k;
	}
    return 0;
}