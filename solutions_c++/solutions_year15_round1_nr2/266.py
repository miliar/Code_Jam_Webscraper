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

int F[100047];
int A[1234];

int GCD(int A, int B) {
    return B ? GCD(B, A % B) : A;
}

int Q[5];

int main() {
    int T, B, N;
    scanf("%d", &T);
    FOR(t,T) {
        scanf("%d %d", &B, &N);
        int LCA = 1;
        FOR(i,B) {
            scanf("%d", &A[i]);
            LCA = LCA * A[i] / GCD(LCA, A[i]);
        }
        int M = 0;
        FOR(i,B) {
            M += LCA / A[i];
        }
        FOR(i,B) Q[i] = 0;
        N %= M; if (N == 0) N = M;
        while (true) {
            FOR(j,B) {
                if (Q[j] == 0) {
                    Q[j] = A[j];
                    if (--N == 0) {
                        printf("Case #%d: %d\n", t+1, j+1);
                        goto next;
                    }
                }
                Q[j]--;
            }
        }
        next:;
    }
    return 0;
}

