#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define FORE(i,v) for(typeof((v).begin())i=(v).begin();i!=(v).end();i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define pf printf
typedef long long ll;
using namespace std;

int R, C, H[200][200], K[200][200];

int getmax(int r, int c, int dr, int dc) {
    int m = 0;
    while (INRANGE(r, c, R, C)) {
        m = max(m, H[r][c]);
        r += dr; c += dc;
    }
    return m;
}

void cut(int r, int c, int dr, int dc, int h) {
    while (INRANGE(r, c, R, C)) {
        K[r][c] = min(K[r][c], h);
        r += dr; c += dc;
    }
}

void tc() {
    scanf("%d%d", &R, &C);
    FOR(r, R) FOR(c, C)
        scanf("%d", &H[r][c]);
    fill(K[0], K[200], 100);
    FOR(r, R) cut(r, 0, 0, 1, getmax(r, 0, 0, 1));
    FOR(c, C) cut(0, c, 1, 0, getmax(0, c, 1, 0));
    FOR(r, R) FOR(c, C)
        if (H[r][c] != K[r][c]) {
            printf("NO\n");
            return;
        }
    printf("YES\n");
}


int main() {
	//freopen(".in", "r", stdin); freopen(".out", "w", stdout);
    int t;
	scanf("%d", &t);
    FORO(i, t) {
        printf("Case #%d: ", i);
        tc();
    }
}


