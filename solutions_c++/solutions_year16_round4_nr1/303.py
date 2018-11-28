#include "iostream"
#include "algorithm"
#include "vector"
#include "set"
#include "map"
#include "cstring"
#include "string"
#include "vector"
#include "cassert"
#include "queue"
#include "cstdio"
#include "cstdlib"
#include "ctime"
#include "cmath"
#include "bitset"

using namespace std;

typedef long long ll;
typedef pair < int, int > ii;

const int N = (1 << 12) + 5;

int n, r, p, s;
ii ch[555];

string build(int x, int n) {
    if(n == 0) {
        string s = "";
        s += (char) x;
        return s;
    }
    string l = build(ch[x].first, n - 1), r = build(ch[x].second, n - 1);
    if(l > r)
        swap(l, r);
    return l + r;
}

bool check(string str) {
    int rr = 0, pp = 0, ss = 0;
    for(int i = 0; i < str.size(); i++) {
        if(str[i] == 'R') rr++;
        if(str[i] == 'P') pp++;
        if(str[i] == 'S') ss++;
    }
    return r == rr and p == pp and s == ss;
}

void solve() {
    scanf("%d %d %d %d", &n, &r, &p, &s);
    string s1 = build('R', n);
    string s2 = build('P', n);
    string s3 = build('S', n);
    string ans = "";
    if(check(s1) and (ans == "" or s1 < ans)) ans = s1;
    if(check(s2) and (ans == "" or s2 < ans)) ans = s2;
    if(check(s3) and (ans == "" or s3 < ans)) ans = s3;
    if(ans == "")
        puts("IMPOSSIBLE");
    else
        puts(ans.c_str());
}

string a[13][3];

int main () {
    
    ch['R'] = {'R', 'S'};
    ch['P'] = {'P', 'R'};
    ch['S'] = {'S', 'P'};
    
    freopen("A-large.in.txt", "r", stdin);
    freopen("largeA.txt", "w", stdout);
    
    int tt;
    
    scanf("%d", &tt);
    
    for(int it = 1; it <= tt; it++) {
        printf("Case #%d: ", it);
        solve();
    }
    
    return 0;
    
}