#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <bitset>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define pb push_back
#define mp make_pair
#define EPS 1.0e-8
#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef long double ld;

char s[1005];

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    int T;
    int smax, ppl, ans;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d %s", &smax, s);

        ans = ppl = 0;
        for(int i=0; i<=smax; i++) {
            if (ppl < i) {
                ans += i - ppl;
                ppl += i - ppl;
            }
            ppl += s[i] - '0';
        }

        printf("Case #%d: %d\n", ncase, ans);
    }

    return 0;
}
