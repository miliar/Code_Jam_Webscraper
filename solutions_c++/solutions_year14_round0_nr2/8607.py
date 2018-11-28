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

int main() {
    int T;
	scanf("%d", &T);
    FORTO(t,1,T) {
        double C, F, X, T = 0.0;
        scanf("%lf %lf %lf", &C, &F, &X);
        int K = max(0.0, (X * F - 2.0 * C) / (C * F));
        FOR(i,K) T += 1 / (2 + i * F);
        printf("Case #%d: %.7lf\n", t, C * T + X / (2.0 + K * F));
	}
	return 0;
}

