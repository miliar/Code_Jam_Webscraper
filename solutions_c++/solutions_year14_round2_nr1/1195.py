#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

vector<string> strs;
#define INF (1<<29)

int trans(string a, string b) {
    // a to b
    if (a == b) return 0;
    int hsa[256] = {0};
    int hsb[256] = {0};
    REP(i, 0, a.size()) hsa[a[i]]++;
    REP(i, 0, b.size()) hsb[b[i]]++;
    REP(i, 0, 256) if ((hsa[i] && !hsb[i]) || (!hsa[i] && hsb[i])) {
        return INF;
    }
    int ret = 0;
    int ia = 0, ib = 0;
    while (ia < a.size() && ib < b.size()) {
        if (a[ia] == b[ib]) {
            int c = a[ia];
            int cnta = 0, cntb = 0;
            while (ib < b.size() && b[ib] == c) ib++, cntb++;
            while (ia < a.size() && a[ia] == c) ia++, cnta++;
            ret += abs(cnta - cntb);
        } else return INF;
    }
    if (ia < a.size() || ib < b.size()) return INF;
    return ret;
}

void build(int at, string cur, const string& s, vector<string> &ret) {
    if (at == s.size()) {
        ret.PB(cur);
        return;
    }
    int c = s[at];
    int is = at;
    int nxt = at;
    while (nxt < s.size() && s[nxt] == c) nxt++;
    while (is < s.size() && s[is] == c) {
        cur += s[at];
        build(nxt, cur, s, ret);
        is++;
    }
}

int solve(int chosen) {
    int n = strs.size();
    string cho = strs[chosen];
    vector<string> pstrs;
    pstrs.PB(cho);
    int ret = INF;
    REP(i, 0, pstrs.size()) {
        int res = 0;
        REP(j, 0, n) {
            res += trans(strs[j], pstrs[i]);
            if (res > INF) break;
        }
        ret = min(ret, res);
    }
    //cout<<ret<<"\n";
    return ret;
}

int main() {
    clock_t startTime = clock();
    ios_base::sync_with_stdio(false);

    int ttt; cin>>ttt;
    REP(test, 1, ttt+1) {
        int n; cin>>n;
        strs.clear();
        REP(i, 0, n) {
            string s; cin>>s;
            strs.PB(s);
        }
        int ans = INF;
        REP(i, 0, n) {
            ans = min(ans, solve(i));
        }
        cout<<"Case #"<<test<<": ";
        if (ans < INF) {
            vector<int> ix(n, 0);
            int bans = 0;
            while (ix[0] < strs[0].size()) {
                int c = strs[0][ix[0]];
                vector<int> pix = ix;
                REP(i, 0, n) {
                    while (ix[i] < strs[i].size() &&
                           strs[i][ix[i]] == c) {
                        ix[i]++;
                    }
                    //ix[i]++;
                }
                vector<int> use;
                REP(i, 0, n) {
                    use.PB(ix[i] - pix[i]);
                }
//                cout<<(char)c<<"\n";
//                REP(i, 0, n) {
//                    cout<<strs[i]<<" "<<ix[i]<<" "<<pix[i]<<" "<<use[i]<<"\n";
//                }
                int mx = *max_element(use.begin(), use.end());
                int best = INF;
                REP(i, 1, mx+1) {
                    int cost = 0;
                    REP(j, 0, n) {
                        cost += abs(i - use[j]);
                    }
                    //cout<<i<<" "<<cost<<"\n";
                    best = min(best, cost);
                }
                bans += best;
            }
            //cout<<ans<<" "<<bans<<"\n";
            ans = min(ans, bans);
            cout<<ans<<"\n";
        }
        else cout<<"Fegla Won\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

