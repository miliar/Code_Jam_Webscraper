#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

#define INF (int)1e9
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int) (x).size())
#define iter(x) __typeof(x.begin())
#define REP(i,x) for(iter(x)i=x.begin();i!=x.end();i++)
#define prs(x) printf("Case #%d: %s\n",Case,x);
#define prd(x) printf("Case #%d: %d\n",Case,x);

int main() {
	
	int TotalCases;
	scanf("%d", &TotalCases);

	for ( int Case = 1; Case <= TotalCases; Case++ ) {
		int R1, R2;
		int A[4][4], B[4][4];
		scanf("%d",&R1);
		for ( int i = 0; i < 4; i++ ) {
			for ( int j = 0; j < 4; j++ ) {
				scanf("%d",&A[i][j]);
			}
		}
		scanf("%d",&R2);
		for ( int i = 0; i < 4; i++ ) {
			for ( int j = 0; j < 4; j++ ) {
				scanf("%d",&B[i][j]);
			}
		}
		int cnt = 0, pos = -1;
		for ( int i = 0; i < 4; i++ ) {
			for (int j = 0; j < 4; j++ ) {
				if ( A[R1-1][i] == B[R2-1][j] ) {
					cnt++;
					pos = A[R1-1][i];
				}
			}
		}
		if ( cnt == 0 )
			prs("Volunteer cheated!");	
		if ( cnt == 1 )
			prd(pos);
		if ( cnt > 1 )
			prs("Bad magician!");
	}

	return 0;
}
