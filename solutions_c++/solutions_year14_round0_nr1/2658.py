//darknife header
#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,n,m) for(int i = (int)n; i <= (int)m; i++)
#define FOD(i,n,m) for(int i = (int)n; i >= (int)m; i--)
#define EACH(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

typedef long long i64;
typedef pair<int, int> PI;

#define sz(v) ((i64)(v).size())
#define all(v) (v).begin(),(v).end()
#define bit(n) (1LL<<(i64)(n))

#define PB push_back
#define MP make_pair
#define X first
#define Y second
template<class T> void fmax(T &a, const T &b) { if (a < b) a = b; }
template<class T> void fmin(T &a, const T &b) { if (a > b) a = b; }
template<class T> T sqr(const T &a) { return a * a; }
//end darknife header
int a[4][4];
int b[4][4];
int i,j,k;
int result;
int m, n;

int check(int rx, int x[4][4], int ry, int y[4][4])
{
	int count = 0;
	FOR(i, 0, 3)
		FOR(j, 0, 3)
			if (x[rx-1][i] == y[ry-1][j]) {
				count++;
				result = x[rx-1][i];
			}
	return count;
}

int main() {
	int Te;
	scanf("%d", &Te);
	for (int Ti = 1; Ti <= Te; Ti++) {
		result = 0;
		cin >> m;
		memset(a, 0, sizeof(a));
		FOR(i, 0, 3) 
			FOR(j, 0, 3)
				cin >> a[i][j];
		cin >> n;
		memset(b, 0, sizeof(b));
		FOR(i, 0, 3)
			FOR(j, 0, 3)
				cin >> b[i][j];
		
		int c = check(m, a, n, b);
		if (c == 1)
			printf("Case #%d: %d\n", Ti, result);
		else if(c > 1)
			printf("Case #%d: Bad magician!\n", Ti);
		else
			printf("Case #%d: Volunteer cheated!\n", Ti);

	}
	return 0;
}
