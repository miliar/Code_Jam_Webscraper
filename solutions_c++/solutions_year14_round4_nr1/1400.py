#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define fr(i,a,b) for(int i = (a); i < (b); ++i)
#define rep(i,n) fr(i,0,n)
#define cl(a,b) memset((a), (b), sizeof(a))
#define all(c) (c).begin(), (c).end()
#define _ << ", " <<
#define db(x) cerr << #x " == " << x << endl

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long long ll;
const int inf = 0x3f3f3f3f;

int n, x;

int A[10010];

int main() {
    int t;
    scanf("%d", &t);
    
    rep(tc, t) {
        printf("Case #%d: ", tc+1);
        
        scanf("%d %d", &n, &x);
        
        rep(i,n) scanf("%d", &A[i]);
        
        sort(A,A+n);
        
        int i = 0, j = n-1;
        int ans = 0;
        while (i <= j) {
            if (i == j) { ++ans; ++i; --j; continue; }
            if (A[i] + A[j] <= x) { ++ans; ++i; --j; }
            else { ++ans; --j; }
        }
        printf("%d\n", ans);
    }

    return 0;
}
