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

string testprefix = "C-large";

void solveTest() {
    int n, m;
    string zip[50];
    int a[50][50] = {0};

    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> zip[i];
    while (m--) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        a[x][y] = a[y][x] = 1;
    }

    if (n == 1) {
        cout << zip[0] << endl;
        return;
    }

    int p[8];
    for (int i = 0; i < n; i++) p[i] = i;

    string res = "";
    // do {
    //     bool can = true;
    //     string cur = "";
    //     for (int i = 0; i < n; i++)
    //         cur += zip[p[i]];

    //     int at = p[0];
    //     int next = 1;
    //     stack<int> track;
        // while (next < n) {
        //     if (a[at][p[next]]) {
        //         track.push(at);
        //         at = p[next];
        //         next += 1;
        //     }
        //     else {
        //         if (track.size() == 0) {
        //             can = false;
        //             break;
        //         }
        //         else {
        //             int x = track.top();
        //             track.pop();
        //             at = x;
        //         }
        //     }
        // }

    //     if (can) {
    //         if (res == "" || cur < res) res = cur;
    //     }
    // } while (next_permutation(p, p + n));

    int mn = 0;
    for (int i = 1; i < n; i++)
        if (zip[i] < zip[mn]) mn = i;

    bool vis[50] = {0};
    vis[mn] = true;

    vector<int> route(n, -1);
    route[0] = mn;

    for (int i = 1; i < n; i++) {
        int best = -1;
        for (int j = 0; j < n; j++) {
            if (vis[j]) continue;
            route[i] = j;

            int at = mn;
            stack<int> track;
            int next = 1;

            bool seen[50] = {false};
            seen[mn] = true;

            bool can = true;
            while (next < route.size()) {
                bool found = false;
                for (int k = 0; k < n; k++)
                    if (!seen[k] && (route[next] == -1 || k == route[next])) {
                        if (a[at][k]) {
                            seen[k] = true;
                            track.push(at);
                            at = k;
                            next += 1;
                            found = true;
                            break;
                        }
                    }

                if (!found) {
                    if (track.size() == 0) {
                        can = false;
                        break;
                    }
                    else {
                        int x = track.top();
                        track.pop();
                        at = x;
                    }
                }
            }

            if (can) {
                if (best == -1 || zip[j] < zip[best])
                    best = j;
            }
        }

        vis[best] = true;
        route[i] = best;
    }

    for (int i = 0; i < route.size(); i++) res += zip[route[i]];

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
