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

int T, N;

struct Point {
    ll x, y;
};

Point P[3456];

int I[3456];

double A[9456];
double M[9456];

bool cmp(int a, int b) {
    if (M[a] < 1e-9) return false;
    if (M[b] < 1e-9) return true;
    if (abs(A[a]-A[b]) < 1e-9) {
        return M[a] < M[b];
    } else {
        return A[a] < A[b];
    }
}

int main() {
    scanf("%d", &T);
    FOR(t,T) {
        printf("Case #%d:\n", t+1);
        scanf("%d", &N);
        FOR(i,N) scanf("%lld %lld", &P[i].x, &P[i].y);
        if (N <= 3) {
            FOR(i,N) printf("0\n");
            continue;
        }
        FOR(i,N) I[i] = i;
        FOR(i,N) {
            FOR(j,N) {
                double dx = P[j].x - P[i].x;
                double dy = P[j].y - P[i].y;
                A[j] = atan2(dy, dx);
                M[j] = dy * dy + dx * dx;
            }
            sort(I, I+N, cmp);
            FOR(j,N-1) {
                double dx = P[I[j]].x - P[i].x;
                double dy = P[I[j]].y - P[i].y;
                A[j] = atan2(dy, dx);
                A[j+N-1] = atan2(dy, dx)+2*M_PI;
                A[j+N+N-1-1] = atan2(dy, dx)+2*M_PI;
            }
            int k = 0;
            int r = N;
            FOR(j,N-1) {
                while (A[j]+M_PI >= A[k]-1e-9) k++;
                r = min(r, N-1-(k-j));
            }
            printf("%d\n", r);
        }
    }
    return 0;
}

