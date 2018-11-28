#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;
typedef long long ll;
const int INF = 987654321;
const ll LINF = 1e15;

bool isPalin (ll val) {
    char str[20]; sprintf(str, "%lld", val);
    char str2[20]; reverse(str2, str2 + sprintf(str2, str));
    return !strcmp(str, str2);
}

void precalc();

int TC, TCC;
ll L[100000]; int LN;

int solve (ll v) {
    int left = 1, right = LN, ret = 0;
    while(left <= right) {
        int mid = (left + right) >> 1;
        if(L[mid] <= v) left = mid + 1, ret = mid;
        else right = mid - 1;
    }
    return ret;
}

int main() {
    freopen("input.txt", "r", stdin);

    int i, j, k;

    precalc();
    freopen("output.txt", "w", stdout);
//    for(i = 1; i <= LN; i++) printf("%lld ", L[i]);

    scanf("%d", &TC);
    while(++TCC <= TC) {
        printf("Case #%d: ", TCC);

        ll A, B; scanf("%lld%lld", &A, &B);
        printf("%d\n", solve(B) - solve(A - 1));
    }
    return 0;
}

void precalc() {
    for(ll i = 1; i <= 1e7; i++) {
        if(isPalin(i) && isPalin(i * i)) L[++LN] = (i * i);
    }
}
