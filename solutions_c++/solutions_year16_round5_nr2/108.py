#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
template <class T> int size(const T &x) { return x.size(); }
const int INF = 2147483647;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

int cbel[1010];
double cnt[1010];
vi below[1010];
double F[1010];

double fac(int n) {
    if (n < 0) return 0.0;
    return F[n];
    double res = 1.0;
    rep(i,2,n+1){
        res *= i;
    }
    return res;
}

void dfs(int at) {
    cbel[at] = 1;
    cnt[at] = 1.0;
    iter(it,below[at]) {
        dfs(*it);
        cbel[at] += cbel[*it];
        cnt[at] *= cnt[*it];
        cnt[at] /= fac(cbel[*it]);
    }
    cnt[at] *= fac(cbel[at] - 1);
}

int main() {
    F[0] = 1.0;
    rep(i,1,1010) F[i] = i * F[i-1];
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n;
        cin >> n;
        vi p(n+1);
        rep(i,0,n+1) below[i].clear();
        rep(i,0,n) {
            cin >> p[i+1];
            below[p[i+1]].push_back(i+1);
        }
        // rep(i,0,n+1) {
        //     cout << "below " << i << ": ";
        //     iter(jt,below[i]) {
        //         cout << *jt << " ";
        //     }
        //     cout << endl;
        // }
        dfs(0);
        // cout << cnt[0] << endl;
        string s;
        cin >> s;
        int m;
        cin >> m;
        vector<string> sub(m);
        rep(i,0,m) {
            cin >> sub[i];
        }
        int its = 50000;
        vi fnd(m);
        rep(jt,0,its) {
            stringstream ss;
            vi avail = below[0];
            while (!avail.empty()) {
                // cout << size(avail) << " " << avail[0] << endl;
                double left = 1.0;
                int sm = 0;
                double all = 1.0;
                iter(it,avail) {
                    left *= cnt[*it];
                    left /= fac(cbel[*it]);
                    sm += cbel[*it];
                    // left += cnt[*it];
                    // all *= cnt[*it];
                }
                left *= fac(sm);
                double at = rand() * 1.0 / RAND_MAX * left;
                int take = 0;
                // cout << "avail ";
                // rep(i,0,size(avail)) {
                //     cout << avail[i] << " ";
                // }
                // cout << endl;
                // cout << "cnt ";
                // rep(i,0,size(avail)) {
                //     cout << cnt[avail[i]] << " ";
                // }
                // cout << endl;
                // cout << "left = " << left << endl;
                // cout << "at = " << at << endl;
                while (true) {
                    int cur = avail[take];
                    double here = 1.0;
                    int sm2 = 0;
                    rep(i,0,size(avail)) {
                        int nxt = avail[i];
                        here *= cnt[nxt];
                        int sz = cur == nxt ? cbel[nxt] - 1 : cbel[nxt];
                        here /= fac(sz);
                        sm2 += sz;
                    }
                    here *= fac(sm2);
                    // cout << "here " << cur << " " << here << endl;
                    // double here = all * fac(sm-1)/fac(sm-cnt[cur]-1);
                    if (at < here) break;
// at > cnt[avail[take]]
                    at -= here;
                    // at -= cnt[avail[take]];
                    take++;
                }
                int who = avail[take];
                // cout << "taking " << who << endl;
                ss << s[who-1];
                swap(avail[take], avail[size(avail)-1]);
                avail.pop_back();
                // cout << size(avail) << endl;
                iter(it,below[who]) {
                    avail.push_back(*it);
                    // cout << "adding " << *it << endl;
                }
            }
            string cur = ss.str();
            rep(i,0,m) {
                if (cur.find(sub[i]) != string::npos) {
                    fnd[i]++;
                }
            }
        }
        printf("Case #%d:", t+1);
        rep(i,0,m) {
            printf(" %0.2lf", 1.0 * fnd[i] / its);
        }
        printf("\n");
    }
    return 0;
}

