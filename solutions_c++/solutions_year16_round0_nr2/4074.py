#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <utility>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

template <class T>
inline int RD(T &x) {
    x = 0;
    char ch = getchar();
    while(!isdigit(ch)) { ch = getchar();  if(ch == EOF) return 0; }
    while(isdigit(ch)) { x *= 10; x += ch - '0'; ch = getchar(); }
    return 1;
}

template <class T>
void PT(T a) {
     if(a > 9) PT(a / 10);
     putchar(a % 10 + '0');
}

const int MAXN = 110;
char str[MAXN];
int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int t, cas = 0;
    RD(t);
    while(t--) {
        scanf("%s", str);
        int len = strlen(str), cur = 0, ans = 0;
        while(cur < len) {
            while(cur < len && str[cur] == '+') cur++;
            if(cur < len) {
                while(cur < len && str[cur] == '-') cur++;
                ans += 2;
            }
        }
        if(ans && str[0] == '-')
            ans--;
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
