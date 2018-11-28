#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define For(i, n) for (int i = 0; i < (int) n; ++i)
#define SIZE(x) ((int) (x).size())
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef DG
#define DG 0
#endif
#define LOG(...) (DG ? fprintf(stderr, __VA_ARGS__) : 0)

int main(){
    int t;
    cin >> t;
    For(cases, t) {
        ll n;
        cin >> n;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", cases + 1);
            continue;
        }
        vector <bool> found_digit(10, false);
        for (ll i = 1;; i++) {
            ll newn = n * i;
            while (newn > 0) {
                found_digit [newn % 10] = true;
                newn /= 10;
            }
            if (find(found_digit.begin(), found_digit.end(), false) == found_digit.end()) {
                printf("Case #%d: %lld\n", cases + 1, i*n);
                break;
            }
        }
    }
}
