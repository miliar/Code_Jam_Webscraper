#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

const int maxn = 12;

int n, r, p, s;
std::string x[(1<<maxn) * 2 + 5];

void clear() {
}

void go(int i, int r, int p, int s) {
    if (r+p+s == 2) {
        x[i] = "";
        if (r) x[i] += 'R';
        if (p) x[i] += 'P';
        if (s) x[i] += 'S';
        std::sort(x[i].begin(), x[i].end());
    } else {
        if ((r&1) && (p&1)) {
            go(i*2+1, r/2, p - p/2, s/2);
            go(i*2+2, r - r/2, p/2, s/2);
        } else if ((r&1) && (s&1)) {
            go(i*2+1, r/2, p/2, s - s/2);
            go(i*2+2, r - r/2, p/2, s/2);
        } else {
            assert((p&1) & (s&1));
            go(i*2+1, r/2, p/2, s - s/2);
            go(i*2+2, r/2, p - p/2, s/2);
        }
        if (x[i*2+2] < x[i*2+1]) x[i] = x[i*2+2] + x[i*2+1];
        else x[i] = x[i*2+1] + x[i*2+2];
    }
}

int main() {
    int testcases; scanf("%d", &testcases);
    for (int testnum = 1; testnum <= testcases; testnum++) {
        printf("Case #%d: ", testnum);
        scanf("%d%d%d%d", &n, &r, &p, &s);
        if (std::max(std::max(r, p), s) <= std::min(std::min(r, p), s) + 1) {
            go(0, r, p, s);
            printf("%s\n", x[0].c_str());
        } else printf("IMPOSSIBLE\n");
        clear();
    }
}

