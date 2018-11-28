#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

const int INF = 1<<29;

int n;
vector<LL> sent[1000];
char s[100000];
char t[100000];

LL encode(string s) {
    LL ret = 0;
    FOR(i, 0, s.size()) {
        ret = ret * 27 + (s[i] - 'a' + 1);
    }
    return ret;
}


map<LL, int> lang[2];
int ans;

void go(int k, int c, int common) {
    if (k == n) {
        ans = min(ans, common);
        return;
    }

    if (k == 0 && c == 1) return;
    if (k == 1 && c == 0) return;

    FOR(j, 0, sent[k].size()) {
        LL t = sent[k][j];
        lang[c][t] += 1;
        if (lang[c][t] == 1) {
            if (lang[c ^ 1][t] > 0) {
                common += 1;
            }
        }
    }

    go(k + 1, 0, common);
    go(k + 1, 1, common);

    FOR(j, 0, sent[k].size()) {
        LL t = sent[k][j];
        lang[c][t] -= 1;
        if (lang[c][t] == 0) {
            if (lang[c ^ 1][t] > 0) {
                common -= 1;
            }
        }
    }
}


int main() {
    int T; gets(s); sscanf(s, "%d", &T); FOE(ca, 1, T) {
        gets(s); sscanf(s, "%d", &n);
        lang[0].clear();
        lang[1].clear();
        FOR(i, 0, n) {
            sent[i].clear();
            gets(s);
            for (int add = 0, off = 0; sscanf(s + off, "%s%n", t, &add) != EOF; off += add) {
                sent[i].PB(encode(t));
            }
        }

        ans = INF;
        go(0, 0, 0);
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
