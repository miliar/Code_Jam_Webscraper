#include <map> 
#include <set> 
#include <list> 
#include <cmath> 
#include <ctime> 
#include <stack> 
#include <queue> 
#include <vector> 
#include <cstdio> 
#include <string> 
#include <bitset> 
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <algorithm> 
#define sqr(x) ((x)*(x)) 
#define ABS(x) ((x<0)?(-(x)):(x)) 
#define eps (1e-9) 
#define mp make_pair 
#define pb push_back 
#define Pair pair<int,int> 
#define xx first 
#define yy second 
#define equal(a,b) (ABS(a-b)<eps) 
using namespace std; 
 
template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();} 
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; } 
 
int dx[8]={0, 0, 1,-1, 1, 1,-1,-1}; 
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1}; 
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2}; 
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1}; 
 
/////////////////////////////////////////////////////////////////////////////////////////////////////

string testprefix = "B-large";

int a, b, k;

long long memo[32][2][2][2];

long long solve(int d, int freeA, int freeB, int freeK) {
    if (d == -1) {
        return 1;
    }
    long long &res = memo[d][freeA][freeB][freeK];
    if (res != -1)
        return res;

    res = 0;
    // 0 0
    int a2, b2, k2;
    a2 = freeA | (a >> d & 1);
    b2 = freeB | (b >> d & 1);
    k2 = freeK | (k >> d & 1);
    res += solve(d - 1, a2, b2, k2);

    // 0 1
    a2 = freeA | (a >> d & 1);
    b2 = freeB;
    k2 = freeK | (k >> d & 1);
    if (freeB || (b >> d & 1) == 1) res += solve(d - 1, a2, b2, k2);

    // 1 0
    a2 = freeA;
    b2 = freeB | (b >> d & 1);
    k2 = freeK | (k >> d & 1);
    if (freeA || (a >> d & 1) == 1) res += solve(d - 1, a2, b2, k2);

    // 1 1
    a2 = freeA;
    b2 = freeB;
    k2 = freeK;
    if (freeA || (a >> d & 1) == 1)
        if (freeB || (b >> d & 1) == 1)
            if (freeK || (k >> d & 1) == 1)
                res += solve(d - 1, a2, b2, k2);
    return res;
}

void solveTest() {
    memset(memo, -1, sizeof(memo));
    cin >> a >> b >> k;
    a--, b--, k--;
    long long res = solve(30, 0, 0, 0);
    cout << res << endl;
}

int main() {
    freopen((testprefix + ".in").c_str(), "r", stdin);
    freopen((testprefix + ".out").c_str(), "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solveTest();
    }
    return 0;
}
