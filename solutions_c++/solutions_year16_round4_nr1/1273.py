#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <stack>

using namespace std;

//global constants
const int INF = 1<<29;
const double EPS = 1e-8;
typedef __int64 LL;
typedef struct Edge {
    int v;
    Edge *next;
} Edge;

//local constants
const int N = 1010;

bool win(int r, int p, int s, string str) {
    int cnt[3] = {};
    for (int i = 0; i < str.size(); ++i) {
        if (str[i] == 'R') cnt[0]++;
        if (str[i] == 'P') cnt[1]++;
        if (str[i] == 'S') cnt[2]++;
    }
    return cnt[0] == r && cnt[1] == p && cnt[2] == s;
}

int main()
{
    freopen("A-large.in","r",stdin);
//    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t, cas = 0;
    scanf(" %d ", &t);


    while (t--) {
        int n, r, p, s;
        scanf("%d %d %d %d", &n, &r, &p, &s);
        printf("Case #%d: ", ++cas);
        n = 1<<n;
        string P = "P";
        string R = "R";
        string S = "S";
        while ((int)P.size() < n) {
            string p1 = P + R;
            string p2 = R + P;
            string r1 = R + S;
            string r2 = S + R;
            string s1 = P + S;
            string s2 = S + P;
            P = p1 < p2 ? p1 : p2;
            R = r1 < r2 ? r1 : r2;
            S = s1 < s2 ? s1 : s2;
        }
        string ans;
        if (win(r, p, s, P)) ans = P;
        else if (win(r, p, s, S)) ans = S;
        else if (win(r, p, s, R)) ans = R;
        else ans = "IMPOSSIBLE";
        printf("%s\n", ans.c_str());
    }
    return 0;
}
