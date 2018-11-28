#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define push_back pb
#define make_pair mp

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define MAXN 1010
char s[MAXN];
int tc, n, sum, ans;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%i%s", &n, s);
        ans = sum = 0;
        for(int i=0; i<=n; ++i) {
            if (sum < i) {
                ans += i - sum;
                sum = i;
            }
            sum += s[i] - '0';
        }
        printf("Case #%i: %i\n", tt, ans);
    }
    return 0;
}