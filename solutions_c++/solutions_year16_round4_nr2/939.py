#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxN = 20;

int n, k;
double p[maxN];
vector <int> h;
int id[maxN];
double res = 0, value = 0;

void Update(int i, int sl) {
    if ((i >= k && sl == 0) || sl == 0) {
        double tmp = 1;
        for(int j = 0; j < k; ++j)
            if (j > i)
                tmp *= p[h[j]];
            else
                tmp *= (id[j] == 1 ? 1 - p[h[j]] : p[h[j]]);
        value += tmp;
        return;
    }
    if (k - i < sl) return;
    id[i] = 1;
    Update(i + 1, sl - 1);
    id[i] = 0;
    Update(i + 1, sl);
}

void Choose(int i, int sl) {
    if ((i > n && sl == 0) || sl == 0) {
        value = 0;
        memset(id, 0, sizeof id);
        Update(0, k >> 1);
        res = max(value, res);
        return;
    }
    if (n - i + 1 < sl) return;
    h.push_back(i);
    Choose(i + 1, sl - 1);
    h.pop_back();
    Choose(i + 1, sl);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int test = 1; test <= nTests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d %d", &n, &k);
        for(int i = 1; i <= n; ++i) scanf("%lf", &p[i]);
        res = 0;
        Choose(1, k);
        printf("%.10lf\n", res);
    }

    return 0;
}
