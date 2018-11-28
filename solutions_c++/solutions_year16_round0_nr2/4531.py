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

int t;
string s;

int dfs(string s) {
    if(s.size() == 0) return 0;
    else if(s.size() == 1) {
        if(s[0] == '+') return 0;
        else return 1;
    }
    else {
        if(s[s.size() - 1] == '-') {
            if(s[0] == '-') {
                reverse(s.begin(), s.end());
                FOR (i, 0, s.size() - 1) {
                    if(s[i] == '-') s[i] = '+';
                    else s[i] = '-';
                }
                return dfs(s) + 1;
            }
            else {
                s[0] = '-';
                reverse(s.begin(), s.end());
                FOR (i, 0, s.size() - 1) {
                    if(s[i] == '-') s[i] = '+';
                    else s[i] = '-';
                }
                return dfs(s) + 2;
            }
        }
        else return dfs(s.substr(0, s.size() - 1));
    }
}

int dfs1(string s) {
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
        return dfs1(s) + 1;
    }
    FOR (i, 0, id - 1) {
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    return dfs1(s) + 1;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        cin >> s;
        cout << "Case #" << i + 1 << ": " << min(dfs(s), dfs1(s)) << endl;
    }
    return 0;
}







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
