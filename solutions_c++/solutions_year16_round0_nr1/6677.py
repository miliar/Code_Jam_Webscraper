#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 1000006
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
using namespace std;
LL values[MAXN];

int main() {
	LL maxi = INT_MIN;
	LL maxj = INT_MIN;
	LD avrJ = 0;
	int maxI = 0;
	FOR (i, 1, MAXN) {
		int mask = 0;
		LL num;
		LL j;
		for (j = 1; ; j++) {
			LL v = j*i;
			num = v;
			if (num > INT_MAX) {
				//puts("alert overflow");
			}
			while (v) {
				mask |= (1<<(v%10));
				v /= 10;
			}
			if (mask == (1<<(10)) - 1 ) {
				break;
			}
		}
		values[i] = num;
		avrJ += j;
		maxj = max(j, maxj);
		if (num > maxi) {
			maxI = i;
		}
		maxi = max(maxi, num);
	}
	//printf("%d\n", (int)(avrJ/(MAXN - 1)));
	//printf("maxj : %lld\n", maxj);
	//printf("maxi: %d %lld\n", maxI, maxi);
	int tc;
	sc1(tc);
	FN (itc, tc) {
		int aux;
		sc1(aux);
		printf("Case #%d: ", (itc + 1));
		if (aux == 0) {
			puts("INSOMNIA");
		} else {
			printf("%lld\n", values[aux]);
		}
	}
}
