// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<(x)<<endl
#define SIZE(X) int(X.size())

int T, A1[4][4], A2[4][4];

int main() {
	scanf("%d", &T);
    FORTO(t,1,T) {
        int r1, r2, r = 0;
        scanf("%d", &r1); r1--; FOR(y,4) FOR(x,4) scanf("%d", &A1[y][x]);
        scanf("%d", &r2); r2--; FOR(y,4) FOR(x,4) scanf("%d", &A2[y][x]);
        FOR(x1,4) FOR(x2,4) if (A1[r1][x1] == A2[r2][x2]) {
            if (r) r = -1; else r = A1[r1][x1];
        }
        printf("Case #%d: ", t);
        if (r == 0)
            printf("Volunteer cheated!\n");
        else if (r == -1)
            printf("Bad magician!\n");
        else
            printf("%d\n", r);
	}
	return 0;
}

