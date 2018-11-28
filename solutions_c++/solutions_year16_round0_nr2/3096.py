#include <bits/stdc++.h>

using namespace std;

#define LOG(...) fprintf(stderr,__VA_ARGS__)
//#define LOG(...)
#define FOR(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort(ALL(c))
#define RSORT(c) sort(RALL(c))

typedef long long ll;
typedef unsigned long long ull;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

int main() {
    int t;
    cin >> t;
    REP(i, t) {
        string s;
        cin >> s;
        int l = s.length();
        vi m(l+1);
        REP(i, l) {
            m[i] = s[i] == '+' ? 1 : 0;
        }
        m[l] = !m[l-1];
        vi r;
        int t = 0, f = 0;
        REP(i, l) {
            if (m[i]) {
                t++;
            } else {
                f++;
            }
            if (m[i] != m[i+1]) {
                if (t > 0) r.push_back(t);
                if (f > 0) r.push_back(f);
                t = 0;
                f = 0;
            }
        }

        int res;
        if (r.size() % 2 == 0) {
            res = m[0] ? r.size() : r.size() - 1;
        } else {
            res = m[0] ? r.size() - 1 : r.size();
        }
        printf("Case #%d: %d\n", i+1, res);
    }
}
