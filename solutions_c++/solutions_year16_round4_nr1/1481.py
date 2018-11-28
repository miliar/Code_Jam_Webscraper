#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

int r, p, s, n;
int x2[20];
char xch[300];
int ch[300];

int check(int a, int b) {
    if (abs(a - b) > 1) { return 1; }
    return 0;
}

void cc(vector<int> &tmp, int nn) {
    int now = nn / 2;
    if (now >= tmp.size()) { return; }
    int i, j, k;
    for (i = 0; i < tmp.size(); i+=nn) {
        rep(j, now) {
            if (xch[tmp[i+j]] > xch[tmp[i+j+now]]) {
                break;
            }
        }
        if (j < now) {
            rep(j, now) {
                swap(tmp[i+j], tmp[i+j+now]);
            }
        }
    }
    cc(tmp, nn + nn);
}

void gogo(vector<int> now) {
    int i, j, k;
    if (now.size() == x2[n]) {
        cc(now, 2);
        rep(k, now.size()) {
            cout << xch[now[k]];
        }
        cout << endl;
        return;
    }
    int nowlen = now.size();
    vector<int> tmp(nowlen*2);
    rep(i, nowlen) {
        j = i+i;
        int www = now[i];
        tmp[j] = www;
        tmp[j+1] = (www+1) % 4;
        if (!tmp[j+1]) { tmp[j+1] = 1; }
    }
    gogo(tmp);
}

void go(int now) {
    vector<int> tmp;
    tmp.push_back(now);
    gogo(tmp);
}

int main() {
    int t, tt, i, j, k;

    x2[0] = 1;
    xrep(i, 1, 15) x2[i] = x2[i-1]*2;
    ch['R'] = 1;
    ch['S'] = 2;
    ch['P'] = 3;
    xch[1] = 'R';
    xch[2] = 'S';
    xch[3] = 'P';

    cin >> tt;
    xrep(t, 1, tt+1) {
        cin >> n >> r >> p >> s;
        cout << "Case #" << t << ": ";
        if (check(r, s) or check(s, p) or check(p, r)) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        while (r + p + s > 1) {
            int w = (r + p + s) % 3;
            int tmp = (r + p + s) / 3;
            if (w == 2) {
                if (r == tmp) {
                    r = p = tmp / 2;
                    s = tmp / 2 + 1;
                }
                else if (p == tmp) {
                    p = s = tmp / 2;
                    r = tmp / 2 + 1;
                }
                else {
                    s = r = tmp / 2;
                    p = tmp / 2 + 1;
                }
            }
            else {
                if (s > tmp) {
                    s = r = tmp;
                    p = tmp - 1;
                }
                else if (r > tmp) {
                    r = p = tmp;
                    s = tmp - 1;
                }
                else {
                    p = s = tmp;
                    r = tmp - 1;
                }
            }
        }
        if (r) { go(ch['R']); }
        else if (s) { go(ch['S']); }
        else { go(ch['P']); }
    }
}
