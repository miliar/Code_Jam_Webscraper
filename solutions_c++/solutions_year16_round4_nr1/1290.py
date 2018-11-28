#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

#define pb push_back
#define mp make_pair

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define DWN(i,h,l) for(int i=(h);i>=(l);--i)
#define MEM(arr, v) memset(arr, v, sizeof(arr))

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> pii;

bool visit[20][5];
string ans[13][3];
string solve(int n, int w) {
    if(visit[n][w]) ans[n][w];
    visit[n][w] = 1;

    if(n == 0) {
        if(w == 0) return ans[n][w] = 'R';
        else if(w == 1) return ans[n][w] = 'P';
        else return ans[n][w] = "S";
    }
    string a1, a2;
    if(w == 0) a1 = solve(n-1, 0), a2 = solve(n-1, 2);
    else if(w == 1) a1 = solve(n-1, 1), a2 = solve(n-1, 0);
    else a1 = solve(n-1, 2), a2 = solve(n-1, 1);

    if(a1 > a2) swap(a1, a2);
    return ans[n][w] = a1 + a2;
}

string solve(int n, int r, int p, int c) {
    REP(i, 3) {
        string s = solve(n, i);
        int num[3] = {0};
        for(char c: s) if(c == 'R') ++num[0];
        else if(c == 'P') ++num[1];
        else ++num[2];
        if(r == num[0] && p == num[1] && c == num[2]) return s;
    }
    return "";
}

int main()
{
	freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int casnum, n, r, p, s;
    memset(visit, 0, sizeof(visit));
    cin >> casnum;
    FOR(cas, 1, casnum) {
        cin >> n >> r >> p >> s;
        printf("Case #%d: ", cas);
        string ret = solve(n, r, p, s);
        if(ret.size()) cout << ret << endl;
        else cout << "Impossible" << endl;
    }

    return 0;
}

