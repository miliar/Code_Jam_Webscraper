#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <vector>
#include <string>
#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define clr(x,y) memset(x,y,sizeof(x))
#define FOR(i,n,m) for (int i = n; i <= m; i++)
#define ROF(i,n,m) for (int i = n; i >= m; i--)

#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;

const ll mod = 1e9 + 7;
const int seed = 105;
const double eps = 1e-8;

/***********************END OF DEFINE******************************/

const int mx = (1 << 16) + 5;

int t, N, J;
ll candidate[505];
ll base_num[505][9];

ll change_base(ll n, int base) {
    ll res = 0;
    ROF (i, N - 1, 0)
        res = res * base + ((n >> i) & 1);
    return res;
}

void get_candidate() {
    int top = 0;
    for (ll i = (1 << (N - 1)) + 1; i <= (1 << N) - 1; i += 2) {
        bool flag = true;
        FOR (j, 2, 10) {
            ll num = change_base(i, j);
            bool subflag = false;
            for (ll k = 2; k <= floor(sqrt(num)); k++) {
                if(num % k == 0) {
                    num = k;
                    subflag = true;
                    break;
                }
            }
            if(subflag)
                base_num[top][j - 2] = num;
            else {
                flag = false;
                break;
            }
        }
        if(flag)
            candidate[top ++] = i;
        if(top == J)
            break;
    }
}
int main() {
    //freopen("C-small-attempt1.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        RII(N, J);
        get_candidate();
        cout << "Case #" << i + 1 << ":" << endl;
        FOR (j, 0, J - 1) {
            ROF (k, N - 1, 0) cout << ((candidate[j] >> k) & 1);
            FOR (k, 0, 8) cout << " " << base_num[j][k];
            cout << endl;
        }
    }
    return 0;
}



/* B
int t;
string s;

int dfs(string s) {
    bool flag = true;
    FOR (i, 0, s.size() - 1) {
        if(s[i] == '-') {
            flag = false;
            break;
        }
    }
    if(flag) return 0;

    int id = -1;
    char c = s[0];
    FOR (i, 0, s.size() - 1) {
        if(s[i] != s[0]) {
            id = i;
            break;
        }
    }
    if(id == -1) {
        FOR (i, 0, s.size() - 1)
            s[i] = '+';
        return dfs(s) + 1;
    }
    FOR (i, 0, id - 1) {
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    return dfs(s) + 1;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        cin >> s;
        cout << "Case #" << i + 1 << ": " << dfs(s << endl;
    }
    return 0;
}
*/


/* A
int t, a[10], cnt = 0;
ll n, tn;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        cin >> n;
        cnt = 0;
        clr(a, 0);
        if(n == 0) {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
            continue;
        }
        int j = 1;
        bool flag = false;
        while(true) {
            tn = j * n;
            while(tn) {
                if(!a[tn % 10]) cnt ++;
                a[tn % 10] = 1;
                tn /= 10;
                if(cnt == 10) {
                    flag = true;
                    break;
                }
            }
            if(flag) break;
            j ++;
        }
        cout << "Case #" << i + 1 << ": " << j * n << endl;
    }
    return 0;
}
*/
