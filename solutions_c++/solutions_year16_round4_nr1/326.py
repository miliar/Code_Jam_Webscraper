#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;

const int maxn = 1e5 + 100;

int p, r, S;
int n;
int len;
char s[2][maxn];

struct node {
    int p, r, s, tag;
    node(int _p = 0, int _r = 0, int _s = 0, int _tag = 0) {
        p = _p;
        r = _r;
        s = _s;
        tag = _tag;
    }
};

node calcu(node t) {
    node ans;
    ans.tag = 0;
    int x = t.p, y = t.r, z = t.s;

    if((y + z - x) % 2 == 0 && (x + z - y) % 2 == 0 && (x + y - z) % 2 == 0) {
        ans.p = (x + y - z) / 2;
        ans.r = (y + z - x) / 2;
        ans.s = (x + z - y) / 2;
        //printf("**  %d\n", ans.s);
        if(ans.p >= 0 && ans.r >= 0 && ans.s >= 0) {
            ans.tag = 1;
        }
    }
    return ans;
}
string work(int h, char ch) {
    string ans = "";
    if(h == 0) {
        ans += ch;
        return ans;
    }
    char ch1, ch2;
    if(ch == 'P') {
        ch1 = 'P';
        ch2 = 'R';
    }
    else if(ch == 'R') {
        ch1 = 'R';
        ch2 = 'S';
    }
    else if(ch == 'S') {
        ch1 = 'P';
        ch2 = 'S';
    }
    string ans1 = work(h - 1, ch1);
    string ans2 = work(h - 1, ch2);
    if(ans1 < ans2) {
        ans = ans1 + ans2;
    } else {
        ans = ans2 + ans1;
    }
    return ans;
}


void solve() {
    node now;
    now = node(p, r, S, 1);
    int flag = 1;
    while(1) {
        //printf("%d  %d  %d\n", now.p, now.r, now.s);
        if(now.tag == 0) {
            flag = 0;
            break;
        }
        if(now.p + now. r + now.s == 1) {
            flag = 1;
            break;
        }
        now = calcu(now);
    }
    if(flag == 0) {
        printf("IMPOSSIBLE\n");
        return;
    }
    int a = 0, b = 1;
    int len = 1;
    if(now.p > 0) {
        s[0][0] = 'P';
    } else if(now.r > 0) {
        s[0][0] = 'R';
    } else if(now.s > 0) {
        s[0][0] = 'S';
    }
    string res = work(n, s[0][0]);
    cout << res << endl;
    /*while(1) {
        if(len == (1 << n)) {
            break;
        }
        int tot = 0;
        for(int i = 0; i < len; i++) {
            if(s[0][i] == 'P') {
                s[1][tot++] = 'P';
                s[1][tot++] = 'R';
            }
            if(s[0][i] == 'R') {
                s[1][tot++] = 'R';
                s[1][tot++] = 'S';
            }
            if(s[0][i] == 'S') {
                s[1][tot++] = 'P';
                s[1][tot++] = 'S';
            }
        }
        for(int i = 0; i < tot; i++) {
            s[0][i] = s[1][i];
        }
        len = tot;
    }
    for(int i = 0; i < (1 << n); i++) {
        printf("%c", s[0][i]);
    }
    printf("\n");*/
}


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("Aout.txt", "w", stdout);
    int ncase;
    scanf("%d", &ncase);
    for(int i = 1; i <= ncase; i++) {
        printf("Case #%d: ", i);
        scanf("%d%d%d%d", &n, &r, &p, &S);
        solve();
    }
    return 0;
}
