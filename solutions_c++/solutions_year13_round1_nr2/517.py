#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

typedef long long LL;
#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

LL v[100000];
LL ans;
LL e, r, n;
void solve(LL cur, LL a, LL g) {
    if (a == n) {
        ans = max(ans, g);
        return;
    }
    for (int i = 0; i <= cur; i++) {
        LL t = cur - i + r;
        if (t > e) t = e;
        LL gain = v[a] * i;
        solve(t, a+1, g+gain);
    }
}

int main() {
    int testCase;
    scanf("%d", &testCase);
    for (int _tests = 1; _tests <= testCase; _tests++) {
        printf("Case #%d: ",_tests);
        cin>>e>>r>>n;
        for (int i = 0; i < n; i++) cin>>v[i];
        ans = 0;
        solve(e, 0, 0);
        cout<<ans<<"\n";
    }

	return 0;
}
