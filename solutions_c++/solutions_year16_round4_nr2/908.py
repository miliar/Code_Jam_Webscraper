#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

int n, k, st[20], top;
double a[20], b[20], res, tmp;

void dfs(int x, double A, int yes, int no) {
    if (x==k) {
        if (yes==no)
            tmp += exp(A);
        return;
    }
    dfs(x+1, A+a[st[x]], yes+1, no);
    dfs(x+1, A+b[st[x]], yes, no+1);
}

double solve() {
    int p = (1 << n) - 1;
    res = 0;
    for (int i = 1; i <= p; ++i) {
        top = 0;
        for (int j = 0; j < n; ++j)
            if ((1<<j)&i) st[top++] = j;
        if (top!=k) continue;
        tmp = 0;
        dfs(0,0,0,0);
        res = max(res,tmp);
    }
    return res;
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t; scanf("%d",&t); int tmp = t;
    while (t--) {
        scanf("%d%d",&n,&k);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            b[i] = log(1-a[i]);
            a[i] = log(a[i]);
        }
        printf("Case #%d: %.7f\n",tmp-t,solve());
    }

    return 0;
}
