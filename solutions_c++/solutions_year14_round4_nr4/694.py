#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define For(i,a,b) for(int i=a;i<=b;i++)
#define For2(i,a,b) for(int i=a;i<b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define OUT(x) {cout << #x << " = " << x << endl;}
#define FOUT(x,a,b) {cout << #x << " = "; For(_,a,b) cout << x[_] << ' '; cout << endl;}
#define FOUT2(x,a,b,c,d) {cout << #x << " = " << endl; For(_,a,b){For(__,c,d) cout << x[_][__] << " "; cout << endl;}}
#define fi first
#define se second
#define mp make_pair
#define sz(x) (int)x.size()
#define BIT(s,i) ((s&(1<<i))>0)

typedef long long ll;

int m, n;
string s[10];
int next[111][30], cnt;
int num[11], res, cres;

int countNode(vector<string> v) {
    //FOUT(s, 0, s.size() - 1);
    For(i, 0, 110) For(j, 0, 29) next[i][j] = 0;
    cnt = 1;
    For2(i, 0, v.size()) {
        int cur = 1;
        For2(j, 0, v[i].size()) {
            if (next[cur][v[i][j] - 'A'] == 0) {
                cnt++;
                next[cur][v[i][j] - 'A'] = cnt;
            }
            cur = next[cur][v[i][j] - 'A'];
        }
    }
    //OUT(cnt);
    return cnt;
}

void rec(int i) {
    if (i == m + 1) {

        bool h[5];
        For(j, 1, n) h[j] = 0;
        For(j, 1, n)
            For(k, 1, m) {
                if (num[k] == j) {
                    h[j] = 1;
                    break;
                }
            }
        bool ok = 1;
        For(j, 1, n) ok &= h[j];
        if (!ok) return;

        //FOUT(num, 1, m);

        int sum = 0;
        For(j, 1, n) {
            vector<string> v; v.clear();
            For(k, 1, m)
                if (num[k] == j) v.push_back(s[k]);
            //FOUT(s, 0, s.size() - 1);
            sum += countNode(v);
        }
        //OUT(sum);
        if (sum > res) {
            res = sum; cres = 1;
        }
        else if (sum == res) {
            cres++;
        }
        return;
    }
    For(j, 1, n) {
        num[i] = j;
        rec(i + 1);
    }
}

void solve() {
    scanf("%d%d", &m, &n);
    For(i, 1, m) cin >> s[i];
    res = 0; cres = 0;
    rec(1);
    printf("%d %d\n",res, cres);
}

int main() {

#ifndef ONLINE_JUDGE
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    For(i, 1, T) {
        cerr << i << endl;
        printf("Case #%d: ", i);
        solve();
    }

}
