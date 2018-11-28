#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;
const int inf = int(1e9)+7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))


const int MAXN = 20+5;
int A[MAXN], B[MAXN];
int xs[MAXN];
int n;
int ans[MAXN];
bool used[MAXN];

bool haveAns;

void dfs(int th) {
    if (haveAns) {
        return;
    }
    if (n == th) {
        //FOR(i,n) cout<<xs[i]<<" ";
        //cout<<endl;
        for (int i = n-1; i >= 0; i--) {
            
            int mx = 0;
            for (int j = i+1; j < n; j++)
                if (xs[i] > xs[j]) mx = max(mx, B[j]);
          //  cout<<i<<" "<<xs[i]<<" "<<mx+1<<endl;
            if (mx+1 != B[i]) return;
        }
        haveAns = true;
        FOR(i,n) ans[i] = xs[i];
    }
    for (int i = 1; i <= n; i++) if (!used[i]) {
        int mx = 0;
        FOR(j,th) if (i > xs[j]) mx = max(mx, A[j]);
        if (mx+1 == A[th]) {
            used[i] = true;
            xs[th] = i;
       
            dfs(th+1);
            used[i] = false;
        }
        
    }
}
int main()
{
    int caseNum;
    scanf("%d", &caseNum);
    for (int ca = 1; ca <= caseNum; ca++)
    {
        ME(used);
        scanf("%d", &n);
        FOR(i,n) scanf("%d", A+i);
        FOR(i,n) scanf("%d", B+i);
        haveAns = false;
        printf("Case #%d:", ca);
        dfs(0);
        FOR(i,n) printf(" %d", ans[i]);
        printf("\n");
        //print ans
    }
    return 0;
}
