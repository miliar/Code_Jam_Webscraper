/* Trân Vu Lâm */
/*             */
/*             */
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <cstring>
#include <set>
#include <math.h>
#include <map>
#include <stack>
#include <queue>

#define ii pair<int, int>
#define si pair<string, int>
#define is pair<int, string>

#define mp make_pair
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pbp(a,b) push_back(make_pair(a,b))
#define insp(a,b) insert(make_pair(a,b))
#define pb(a) push_back(a)
#define ins(a) insert(a)

#define uint64 unsigned long long
#define int64 long long

#define INF 1071071071
#define Pr 9875321
#define pi 3.1415926535897932384626433832795
#define eps 1e-8
#define maxN 105

using namespace std;
int r, c;
int data[maxN][maxN], mxr[maxN], mxc[maxN], patt[maxN][maxN];

bool check() {
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            if (data[i][j] != patt[i][j])
                return false;
    return true;
}

int main(void) {
    freopen("B-large.in", "r", stdin);
    freopen("B.OUT", "w", stdout);
    int tcs;
    cin>>tcs;
    for (int tcNo = 1; tcNo <= tcs; tcNo++) {
        scanf("%d %d", &r, &c);
        for (int i = 0; i < r; i++) {
            mxr[i] = 0;
            for (int j = 0; j < c; j++) {
                scanf("%d", &patt[i][j]);
                mxr[i] = max(mxr[i], patt[i][j]);
                data[i][j] = 100;
            }
        }
        for (int i = 0; i < c; i++) {
             mxc[i] = 0;
            for (int j = 0; j < r; j++)
                mxc[i] = max(mxc[i], patt[j][i]);
        }

        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                data[i][j] = min(data[i][j], mxr[i]);

        for (int i = 0; i < c; i++)
            for (int j = 0; j < r; j++)
                data[j][i] = min(data[j][i], mxc[i]);
        if (check())
            printf("Case #%d: YES\n", tcNo);
        else printf("Case #%d: NO\n", tcNo);
    }

    return 0;
}
