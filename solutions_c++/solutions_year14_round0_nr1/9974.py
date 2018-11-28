#pragma warning ( disable : 4786 )

#include <iostream>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>

#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
using namespace std;

//#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define _rep( i, a, b, x ) for( i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )

#define ff first
#define ss second

#define pii pair< int, int >
#define psi pair< string, int >

#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define set(p) memset(p, -1, sizeof(p))
#define clr(p) memset(p, 0, sizeof(p))

//typedef long long i64;
//typedef __int64 i64;
typedef long double ld;

//const double pi = (2.0*acos(0.0));
const double pi = acos(-1.0);
const double eps = 1e-9;
const int inf = (1<<28);
const int MAX = 20;

int arr1[MAX][MAX], arr2[MAX][MAX];
int r1, r2;
int flg[MAX];

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-out.txt", "w", stdout);
	
	int i, j, k;
	int test, t = 0, kase=0;
	int cnt, ans;

	scanf("%d", &test);
	while(test--) {
		memset(flg, 0, sizeof(flg));
		cnt = 0;

		scanf("%d", &r1);
		for(i=0; i<4; i+=1) {
			for(j=0; j<4; j+=1) {
				scanf("%d", &arr1[i][j]);
			}
			if(i == r1-1) {
				for(j=0; j<4; j+=1) {
					flg[arr1[i][j]] = 1;
				}
			}
		}

		scanf("%d", &r2);
		for(i=0; i<4; i+=1) {
			for(j=0; j<4; j+=1) {
				scanf("%d", &arr2[i][j]);
			}
			if(i == r2-1) {
				for(j=0; j<4; j+=1) {
					if(flg[arr2[i][j]] == 1) {
						cnt += 1;
						ans = arr2[i][j];
					}
				}
			}
		}

		if(cnt == 0) printf("Case #%d: Volunteer cheated!\n", ++t);
		else if(cnt == 1) printf("Case #%d: %d\n", ++t, ans);
		else printf("Case #%d: Bad magician!\n", ++t);
	}
	return 0;
}
