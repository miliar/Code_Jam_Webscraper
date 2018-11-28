#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
using namespace std;

#define fori(a,b) for(i = a; i <= b; i++)
#define forj(a,b) for(j = a; j <= b; j++)
#define fork(a,b) for(k = a; k <= b; k++)
#define scani(a) scanf("%d",&a);
#define scanlli(a) scanf("%lld", &a);
#define scanc(c) scanf("%c",&c);
#define scans(s) scanf("%s", s);
#define mp(a,b) make_pair(a, b)
#define ll(a) (long long int)(a)
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define println printf("\n");
#define sz(v) v.size()
#define len(s) s.length()
#define max(a,b) ((a > b) ? a : b)
#define min(a,b) ((a < b) ? a : b)

int main() {
    int t, te, ans, i, m, sofar, cnt, inc;
    string str;
    scani(t)
    for(te = 1; te <= t; te++) {
        scani(m)
        cin >> str;
        ans = 0;
        sofar = str[0] - '0';
        fori(1, m) {
            inc = 0;
            cnt = str[i] - '0';
            if (i > sofar && cnt > 0) {
                inc = i - sofar;
            }
            ans += inc;
            sofar += cnt + inc;
        }
        printf("Case #%d: %d\n", te, ans);
    }
    return 0;
}