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

i32 solve(string s) {
    size_t len = s.size();
    string dis = string(len, '+');
    i32 cnt = 0; string tmp;
    size_t right = len-1;
    while (s != dis) {
        if (s[right] == '-') {
            if (s[0] == '+') {
                size_t r = 0;
                while (r < right && s[r+1] == '+') {
                    r++;
                }
                upto(0, r, i) {
                    s[i] = '-';
                }
                cnt++;
            }
            tmp = s;
            upto(0, right, i) {
                s[i] = tmp[right-i] == '-' ? '+' : '-';
            }
            cnt++;
        }
        right--;
    }
    return cnt;
}

i32 main()
{
    i32 t;
    cin >> t;
    vec<string> s(t);
    times(t, i) {
        cin >> s[i];
    }
    times(t, i) {
        i32 ans = solve(s[i]);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}