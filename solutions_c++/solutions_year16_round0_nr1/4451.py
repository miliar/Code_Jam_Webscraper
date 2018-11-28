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
