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

string testprefix = "B-small-attempt3";

int n;
int a[1000];

int solve(vector<int> v) {
    int cnt = 0;
    for (int i = 0; i < v.size(); i++)
        for (int j = i + 1; j < v.size(); j++)
            if (v[i] > v[j]) cnt++;

    return cnt;
}

int brute(vector<int> v) {
    int n = v.size();
    int p[10];
    for (int i = 0; i < n; i++) p[i] = i;
    int res = 1 << 30;
    do {
        int cnt = 0;
        int a[10];
        for (int i = 0; i < n; i++) a[i] = v[p[i]];

        int mx = 0;
        for (int i = 0; i < n; i++) if (a[i] > a[mx]) mx = i;

        bool good = true;
        for (int i = 0; i + 1 < mx; i++) if (a[i] > a[i + 1]) good = false;
        for (int i = mx; i + 1 < n; i++) if (a[i] < a[i + 1]) good = false;
        if (good) {
            cnt = 0;
            for (int i = 0; i < n; i++)
                for (int j = i + 1; j < n; j++)
                    if (p[i] > p[j]) cnt++;
            res = min(res, cnt);
        }
    } while(next_permutation(p, p + n));
    return res;
}

void solveTest() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    // int mx = 0;
    // for (int i = 0; i < n; i++) if (a[i] > a[mx]) mx = i;

    // int big = 2000000001;

    // int res = 1 << 30;
    // for (int i = mx; i < n; i++) {
    //     int cur = 0;
    //     vector<int> v;
    //     for (int j = 0; j < n; j++) {
    //         if (i != -1 && a[j] <= a[i]) v.pb(big - a[j]);
    //         else v.pb(a[j]);
    //     }
    //     res = min(res, solve(v));
    // }

    vector<int> v;
    for (int i = 0; i < n; i++) v.pb(a[i]);

    printf("%d\n", brute(v));
    fflush(stdout);
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
