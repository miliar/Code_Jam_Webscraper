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

string testprefix = "A-large";

int a[10000];
int n, x;

void solveTest() {
    scanf("%d%d", &n, &x);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    sort(a, a + n);
    reverse(a, a + n);

    int count = 0;
    int cur = 0;

    while (true) {
        bool done = true;
        for (int i = 0; i < n; i++) if (a[i]) done = false;
        if (done) break;
        for (int i = 0; i < n; i++) {
            if (a[i] > 0 && cur + a[i] <= x) {
                if (cur > 0) {
                    a[i] = 0;
                    break;
                }
                else {
                    cur += a[i];
                    a[i] = 0;
                }
            }
        }
        cur = 0;
        count += 1;
    }

    printf("%d\n", count);
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
