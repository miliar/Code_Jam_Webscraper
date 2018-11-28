#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <climits>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <sstream>
#include <numeric>
#include <limits>
using namespace std ;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<ll> vl;
typedef vector<vector<long long int> > vvl;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;

template<class T> T gcd(T a,T b) {return ((!b)?(a):gcd(b,a%b));}

const int inf = std::numeric_limits<int>::max();
const ll linf = std::numeric_limits<ll>::max();
const int dir4[4][2] = {{0,1},{-1,0},{0,-1},{1,0}};
const int dir8[8][2] = {{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1}};
const int horseMove[8][2] = {{-1,2},{-2,1},{-2,-1},{-1,-2},{1,-2},{2,-1},{2,1},{1,2}};

#define For( i, a, b )              for(int i = (int)a;i<= (int)b; ++i)
#define tr( iter, a )               for(typeof((a).begin()) iter = (a).begin();iter != (a).end(); ++iter )
#define rtr( iter, a )              for(typeof((a).rbegin()) iter = (a).rbegin();iter != (a).rend(); ++iter )

int solve(int T) {
	int ans, cart, tmp, c1, c2;
	int dd[20];

	memset( dd, 0, sizeof (dd));

	scanf("%d", &c1);
	For (i, 1, 4) {
		For (j, 1, 4) {
			scanf("%d", &tmp);
			if (i == c1) {
				dd[tmp] += 1;
			}
		}
	}
	
	scanf("%d", &c2);
	For (i, 1, 4) {
		For (j, 1, 4) {
			scanf("%d", &tmp);
			if (i == c2) {
				dd[tmp] += 1;
			}
		}
	}

	ans = 0;
	For (i, 1, 16) if (dd[i] == 2) {
		ans += 1;
		cart = i;
	}

	if (ans == 0) {
		printf("Case #%d: Volunteer cheated!\n", T);
	} else if (ans == 1) {
		printf("Case #%d: %d\n", T, cart);
	} else {
		printf("Case #%d: Bad magician!\n", T);
	}
	
	return 0;
}

int main(void) {
#if CONTEST
	freopen("A-small-attempt0.in","rt",stdin);
#endif
	int T;
	scanf("%d", &T);
	For (i, 1, T)
		solve(i);
	
	return 0;
}
