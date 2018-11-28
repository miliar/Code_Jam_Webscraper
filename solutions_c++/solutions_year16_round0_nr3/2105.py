#include <bits/stdc++.h>
using namespace std;
using i32 = int;
using i64 = int64_t;
template <class T> using vec = vector<T>;
using wdgraph = vec<vec<pair<i32, i32>>>;
#define times(n, i) for (i32 i = 0; i < (n); i++)
#define range(n, m, i) for (i32 i = (n); i < (m); i++)
#define upto(n, m, i) for (i32 i = (n); i <= (m); i++)
#define downto(n, m, i) for (i32 i = (n); i >= (m); i--)
#define foreach(xs, x) for (auto &x : (xs))
#define all(xs) (xs).begin(), (xs).end()
#define sortall(xs) sort(all(xs))
#define reverseall(xs) reverse(all(xs))
#define uniqueall(xs) erase(unique(all(xs)), (xs).end())
#define maximum(xs) *max_element(all(xs))
#define minimum(xs) *min_element(all(xs))
i64 MOD = 1000000007;

i64 toi(i64 x, i32 base) {
    i64 ret = 0;
    i32 i = 0;
    while((x >> i) > 0) {
        ret += ((x >> i) & 1)*(pow(base, i));
        i++;
    }
    return ret;
}

i64 getd(i64 x) {
    if (x % 2 == 0)
        return 2;
    if (x % 3 == 0)
        return 3;
    i64 m = 5; bool f = false;
    while (x % m != 0 && m < min(x, 10000ll)) {
        f = !f;
        if (f)
            m += 2;
        else
            m += 4;
    }
    if (m >= min(x, 10000ll)) {
        m = -1; // x is a prime;
    }
    return m;
}

i32 main()
{
    i32 t,n,j;
    cin >> t >> n >> j;

    vec<i64> ans;
    vec<vec<i64>> dss;
    i64 x = 1 + (1 << (n-1));
    range(1, (1 << (n-2)) - 1, c) {
        vec<i64> ds;
        i64 nx = x + (c << 1);
        range(2, 11, b) {
            i64 d = getd(toi(nx, b));
            if (d < 0)
                break;
            ds.emplace_back(d);
        }
        if (ds.size() < 9)
            continue;
        ans.emplace_back(nx);
        dss.emplace_back(ds);
        if (ans.size() >= j)
            break;
    }

    cout << "Case #1:" << endl;
    times(j, i) {
        string s;
        times(n, k) {
            s += to_string((ans[i] >> k) & 1);
        }
        reverseall(s); cout << s;
        times(9, k) {
            cout << " " << dss[i][k];
        } cout << endl;
    }
    return 0;
}