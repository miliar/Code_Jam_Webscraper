#include<stdio.h>
#include<iostream>
#include<string>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<cstring>
#include<algorithm>
#define LL long long
using namespace std;

char s[1010];

int main () {
//    freopen ("in.txt", "r", stdin);
//    freopen ("out.txt", "w", stdout);
    int T, cas = 1;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        scanf ("%s", s);
        int res = 0, sum = 0;
        for (int i = 0; i <= n; i++) {
            if (i > sum) res++, sum = i;
            sum += s[i] - '0';
        }
        printf ("Case #%d: %d\n", cas++, res);
    }
}
