#include <bits/stdc++.h>

using namespace std;

const int MAXN = 400 + 10;

int n, k;
double prob[MAXN];
double f[MAXN][MAXN];

int get_bit(int x, int n) {
    return ((x >> n) & 1);
}

double get_tie_prob(int x) {
    vector<double> p;
    for(int i = 0; i < n; i++)
        if (get_bit(x, i) == 1) p.push_back(prob[i + 1]);
    for(int i = 0; i <= n; i++)
        for(int j = 0; j <= n; j++) f[i][j] = 0.0;
    f[0][0] = 1.0;
    for(int i = 0; i < k; i++)
        for(int j = 0; j <= i; j++) {
            //cout << i << " " << j << " " << f[i][j] << endl;
            f[i + 1][j] += f[i][j] * (1 - p[i]);
            f[i + 1][j + 1] += f[i][j] * p[i];
        }

    return f[k][k / 2];
}

double get_tie_prob(vector<double> &p) {
    for(int i = 0; i <= n; i++)
        for(int j = 0; j <= n; j++) f[i][j] = 0.0;
    f[0][0] = 1.0;
    for(int i = 0; i < k; i++)
        for(int j = 0; j <= i; j++) {
            //cout << i << " " << j << " " << f[i][j] << endl;
            f[i + 1][j] += f[i][j] * (1 - p[i]);
            f[i + 1][j + 1] += f[i][j] * p[i];
        }

    return f[k][k / 2];
}

double equals(double x, double y, double eps = 1e-9) {
    return abs(x - y) <= eps;
}

bool check(int v) {
    vector<int> a(n + n, 0);
    for(int i = 0; i < n; i++) a[i] = a[n + i] = get_bit(v, i);
    for(int i = 0; i < n; i++)
        if (a[i] == 1) {
            bool ok = true;
            for(int j = i; j < i + k; j++)
                if (a[j] == 0) {
                    ok = false;
                    break;
                }
            if (ok) return true;
        }
    return false;

}

void solve() {
    cin >> n >> k;
    for(int i = 1; i <= n; i++) cin >> prob[i];

    sort(prob + 1, prob + 1 + n);

    double res = 0.0;
    vector<int> bi;
    for(int i = 1; i < (1 << n); i++) {
        int num_bits = 0;
        for(int j = 0; j < n; j++) num_bits += get_bit(i, j);
        if (num_bits == k) {
            double x = get_tie_prob(i);
            if (equals(res, x)) {
                bi.push_back(i);
            }
            else if (x > res) {
                res = x;
                bi.clear();
                bi.push_back(i);
            }
        }
    }

    //printf("%.09f\n", res);
    for(int v : bi) {
        //for(int i = 0; i < n; i++) cout << get_bit(v, i); cout << endl;
        if (check(v)) {
            cout << "YES\n";
            return;
        }
    }
    cout << "NO\n";
}

void solve_2() {
    cin >> n >> k;
    for(int i = 1; i <= n; i++) cin >> prob[i];

    sort(prob + 1, prob + 1 + n);

    for(int i = 1; i <= n; i++) prob[n + i] = prob[i];

    double res = 0.0;
    for(int i = 1; i <= n; i++) {
        vector<double> p;
        for(int j = i; j < i + k; j++) p.push_back(prob[j]);
        double x = get_tie_prob(p);
        if (x > res) res = x;
    }
    printf("%.09f\n", res);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int ntests;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; tc++) {
        cout << "Case #" << tc << ": ";
        solve_2();
    }
}
