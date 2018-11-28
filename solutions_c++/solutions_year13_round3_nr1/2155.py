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
#define maxN 1000005

using namespace std;
char s[maxN];

bool check(char c) {
    return c != 'a' && c != 'o' && c != 'e' && c != 'u' && c != 'i';
}

int main(void) {
    freopen("a.INP", "r", stdin);
    freopen("a.OUT", "w", stdout);
    int tcs;
    cin>>tcs;
    for (int tcNo = 1; tcNo <= tcs; tcNo++) {
        int n;
        scanf("%s %d", &s, &n);
        int len = strlen(s);
        int64 ans = 0, bef = 0;
        bool have = false;
        for (int i = 0; i + n <= len; i++) {
            bool found = true;
            for (int j = 0; j < n; j++) {
                if (!check(s[i + j])) {
                    found = false;
                    break;
                }

            }
            if (found) {
                int64 first = i, last = len - i - n;
                //cout<<first<<" "<<last<<endl;
                ans -= (last + 1) * bef;
                bef = i + 1;
                if (min(first, last) == 0) ans += max(first, last) + 1;
                else
                    ans += (first + 1) * (last + 1);
                have = true;
            }
        }
        printf("Case #%d: %d\n", tcNo, ans * have);

    }



    return 0;
}
