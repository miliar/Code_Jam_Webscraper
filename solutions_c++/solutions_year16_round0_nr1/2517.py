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

i32 solve(i32 n) {
    set<i32> d;
    if (n == 0)
        return -1;
    i32 acc = 0;
    while (d.size() < 10) {
        acc += n;
        i32 tmp = acc;
        while (tmp > 0) {
            d.insert(tmp % 10);
            tmp /= 10;
        }
    }
    return acc;
}

i32 main()
{
    i32 t;
    cin >> t;
    vec<i32> n(t);
    times(t, i) {
        cin >> n[i];
    }
    times(t, i) {
        i32 ans = solve(n[i]);
        cout << "Case #" << i+1 << ": " << (ans >= 0 ? to_string(ans) : "INSOMNIA") << endl;
    }
    return 0;
}