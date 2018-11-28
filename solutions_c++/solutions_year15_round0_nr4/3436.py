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
    int t, te, x, r, c, mn, mx, p;
    scani(t)
    for (te = 1; te <= t; te++) {
        scani(x)
        scani(r)
        scani(c)
        mx = max(r, c);
        mn = min(r, c);
        p = r * c;
        
        printf("Case #%d: ", te);
        if (x == 1) {
            printf("GABRIEL");
        } else if (x == 2) {
            if (p % 2 == 1) {
                printf("RICHARD");
            } else {
                printf("GABRIEL");
            }
        } else if (x == 3) {
            if (p == 6 || p == 9 || p == 12) {
                printf("GABRIEL");
            } else {
                printf("RICHARD");
            }
        } else {
            if (p == 12 || p == 16) {
                printf("GABRIEL");
            } else {
                printf("RICHARD");
            }
        }
        printf("\n");
    }
    return 0;
}