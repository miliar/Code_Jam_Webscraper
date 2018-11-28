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

int A[1234];

int main() {
    int T, N;
    scanf("%d", &T);
    FOR(t,T) {
        scanf("%d %d", &N, &A[0]);
        int RA = 0;
        int RB = 0;
        int J  = 0;
        FOR(i,N-1) {
            scanf("%d", &A[i+1]);
            RA += max(0,A[i]-A[i+1]);
            J   = max(J,A[i]-A[i+1]);
        }
        FOR(i,N-1) {
            RB += min(J, A[i]);
        }
        printf("Case #%d: %d %d\n", t+1, RA, RB);
    }
    return 0;
}

