#include <bits/stdc++.h>

using namespace std;

struct Fenwick {
    vector<int> t;
    int n;
    Fenwick(int n) : n(n) {
        t.assign(n, 0);
    }

    int sum (int r)
    {
        int result = 0;
        for (; r >= 0; r = (r & (r+1)) - 1)
            result += t[r];
        return result;
    }

    void inc (int i, int delta)
    {
        for (; i < n; i = (i | (i+1)))
            t[i] += delta;
    }

    int sum (int l, int r)
    {
        return sum (r) - sum (l-1);
    }
};

inline int solve(vector<int> a) {
    int pos = 0;
    int ret = 0;
    char u[a.size()];
    memset(u, 0, sizeof(u));
    while (pos < (int)a.size()) {
        int curma = -1;
        int curpos = -1;
        for (int i = pos; i < (int)a.size(); ++i) {
            if (!u[i]) {
                if (curma < a[i]) {
                    curma = a[i];
                    curpos = i;
                }
            }
        }
        for (int i = curpos; i > pos; --i) {
            swap(a[i], a[i - 1]);
        }
        ret += curpos - pos;
        ++pos;
    }
    return ret;
}
vector<int> bestMa;
inline int solve2(int a[], int n) {
    int ans = INT_MAX;
    for (int mask = 0; mask < (1 << n); ++mask) {
        char u[n];
        int b[n];
        memcpy(b, a, n * sizeof(int));
        memset(u, 0, sizeof(u));

        int curans = 0;
        int curpos = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                int pos;
                for (pos = 0; pos < n; ++pos) {
                    if (b[pos] == i) {
                        break;
                    }
                }
                curans += pos - curpos;
                for (int j = pos; j > curpos; --j) {
                    swap(b[j], b[j - 1]);
                }
                ++curpos;
            }
        }
        vector<int> tmp;
        for (int i = curpos; i < n; ++i) {
            tmp.push_back(b[i]);
        }
        curans += solve(tmp);
        if (curans < ans) {
            ans = curans;
            bestMa.clear();
        }
        if (curans == ans) {
            bestMa.push_back(mask);
        }
    }
    return ans;
}

inline void print(int q, int n) {
    for (int i = 0; i < n; ++i) {
        cout << i;
    }
    cout << endl;
    for (int i = 0; i < n; ++i) {
        cout << ((q >> i) & 1);
    }
    cout << endl;
}

inline void solve(int test) {

    int n;
    cin >> n;
    int a[n];
    int b[n];
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        b[i] = a[i];
    }
    sort(b, b + n);
    for (int i = 0; i < n; ++i) {
        a[i] = lower_bound(b, b + n, a[i]) - b;
    }

    int ans = 0;
    int l = 0, r = n - 1;
    for (int i = 0; i < n; ++i) {
        for (int j = l; j <= r; ++j) {
            if (a[j] == i) {
                if ((j - l) > (r - j)) {
                    for (int k = j; k < r; ++k) {
                        swap(a[k], a[k + 1]);
                        ++ans;
                    }
                    --r;
                } else {
                    for (int k = j; k > l; --k) {
                        swap(a[k], a[k - 1]);
                        ++ans;
                    }
                    ++l;
                }
                break;
            }
        }
    }
    cout << "Case #" << test << ": " << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }

    return 0;
}
