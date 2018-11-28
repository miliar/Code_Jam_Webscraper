#include <sstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdint>

#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <set>

#include <string>

#include <stdint.h>
#include <limits>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
#define FORE(a, b) for(int i = a; i < b; i++)
#define CLR(a, v) memset(a, v, sizeof(a))

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.ot", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t++ < T) {
        ull p, q;
        char ch;
        cin >> p;
        cin >> ch;
        cin >> q;
        int ans = 0;
        int pt = p;
        while (pt < q) {
            pt *= 2;
            ans++;
        }
        int rest = pt - q;
        if (rest != 0) {//check whether add of 2 within ans
            //find div
            int div1 = rest;
            int div2 = q;
            while (div1 != 0) {
                int t = div2 % div1;
                div2 = div1;
                div1 = t;
            }
            q /= div2;
            rest /= div2;

            for (ull i = 1; i <= 40; i++) {
                if (rest && rest * pow(2, i) >= q) {
                    if ((q % (ull) pow(2, i)) == 0)
                        rest -= q / pow(2, i);
                }
            }
            if (rest == 0)
                printf("Case #%d: %d\n", t, ans);
            else
                printf("Case #%d: impossible\n", t);
        } else {
            printf("Case #%d: %d\n", t, ans);
        }
    }
}
