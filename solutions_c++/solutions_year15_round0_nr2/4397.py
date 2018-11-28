#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <sstream>
using namespace std;

#define DB(x) cerr<<#x<<"="<<x<<" "
#define DBN(x) cerr<<#x<<"="<<x<<"\n"
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define sqr(x) ((x)*(x))
#define sz(x) ((int)(x).size())
#define clr(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define mp make_pair

#define lson x+x,l,y
#define rson x+x+1,y+1,r

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<long long, long long> PLL;

#define INF 1000000000
#define EPS (double)1e-9
#define MOD 1000000007
#define PI 3.14159265358979328462
int n;
int a[1111];
void solve()
{
    int T;
    for (int ca = 1; ca <= T; ca++) {
        priority_queue<int> pq;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            pq.push(a[i]);
        }
        int ans = 1111, t = 0;
        while (pq.top() > 1) {
            ans = min(ans, pq.top()+t);
            t++;
            int tp = pq.top(); pq.pop();
            pq.push(tp/2); pq.push(tp-tp/2);
        }
        ans = min(ans, t+1);
        cout << "Case #" << ca <<": "
             << ans << endl;
    }
}
int ans;
set<vector<int> > ha;
void dfs(vector<int> v, int t)
{
    sort(v.begin(), v.end());
    if (ha.count(v)) return;
    ha.insert(v);
    ans = min(ans, t+v[v.size()-1]);
    if (v.back() == 1) {
        return;
    }
    vector<int> vv = v;
    int bk = v.back();
    for (int i = 1; i <= bk/2; i++) {
        vector<int> vv = v;
        vv.pop_back();
        vv.push_back(i);
        vv.push_back(bk-i);
        dfs(vv, t+1);
    }
}

int main(int argc, char *argv[])
{
    int T; cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        cin >> n;
        vector<int> v;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            v.push_back(a[i]);
        }
        ans = 1111;
        ha.clear();
        dfs(v, 0);

        cout << "Case #" << ca <<": "
             << ans << endl;
    }
    return 0;
}

