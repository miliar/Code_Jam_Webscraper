#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

int N, X, s[100000];

void solve() {
    scanf("%d %d", &N, &X);
    for (int i = 0; i < N; ++i)
        scanf("%d", &s[i]);
    sort(s, s + N);
    int ans = 0, front = 0;
    for (int i = N - 1; i >= front; --i) {
        ++ans;
        if (i == front)
            break;
        else if (s[i] + s[front] <= X) {
            ++front;
        }
    }
    printf("%d\n", ans);
}

int main() {
    int numCases;
    scanf("%d", &numCases);
    for (int caseNo = 1; caseNo <= numCases; ++caseNo) {
        printf("Case #%d: ", caseNo);
        solve();
    }
    return 0;
}
