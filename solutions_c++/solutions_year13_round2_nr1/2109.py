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

ii finddis(int a, int k) {
    int cnt = 0;
    while (a <= k) {
        cnt++;
        a += (a - 1);
    }
    return mp(cnt, a + k);
}

int data[maxN], n;

int Try(int mote, int pos) {
    if (pos == n) return 0;
    if (mote > data[pos]) Try(mote + data[pos], pos + 1);
    ii tmp = finddis(mote, data[pos]);
    return min(Try(mote, pos + 1) + 1, Try(tmp.second, pos + 1) + tmp.first);
}


int main(void) {
    freopen("a.INP", "r", stdin);
    freopen("a.OUT", "w", stdout);
    int tcs, mote;
    cin>>tcs;
    for (int tcNo = 1; tcNo <= tcs; tcNo++) {
        scanf("%d %d", &mote, &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &data[i]);
        if (mote == 1) {
            printf("Case #%d: %d\n", tcNo, n);
            continue;
        }
        sort(data, data + n);
        int pos = 0;
        int ans = Try(mote, 0);
        printf("Case #%d: %d\n", tcNo, ans);
    }


    return 0;
}
