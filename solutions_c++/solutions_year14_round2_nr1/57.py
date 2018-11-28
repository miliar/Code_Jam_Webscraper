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

vector<Pair> get(string s) {
    vector<Pair> v;
    int cnt = 0;
    for (int i = 0; i < s.size(); i++) {
        cnt++;
        if (i == s.size() - 1 || s[i] != s[i + 1]) {
            v.pb(mp((int)s[i], cnt));
            cnt = 0;
        }
    }

    return v;
}

void solveTest() {
    string s[100];
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> s[i];

    vector<Pair> v[100], base;
    base = get(s[0]);

    for (int i = 0; i < n; i++) {
        v[i] = get(s[i]);
        bool bad = false;
        if (v[i].size() != base.size())
            bad = true;
        else {
            for (int j = 0; j < base.size(); j++)
                if (v[i][j].first != base[j].first) bad = true;
        }

        if (bad) {
            cout << "Fegla won" << endl;
            return;
        }
    }

    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < v[i].size(); j++) cout << v[i][j].second << " " ;
    //         cout << endl;
    // }

    int res = 0;
    for (int i = 0; i < base.size(); i++) {
        int x = 1 << 30;
        for (int cnt = 1; cnt <= 100; cnt++) {
            int cur = 0;
            for (int j = 0; j < n; j++)
                cur += ABS(v[j][i].second - cnt);
            x = min(x, cur);
        }

        res += x;
    }

    printf("%d\n", res);
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
