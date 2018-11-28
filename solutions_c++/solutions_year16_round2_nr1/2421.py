#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
using namespace std;
using i8  = int8_t;  using u8  = uint8_t;
using i16 = int16_t; using u16 = uint16_t;
using i32 = int32_t; using u32 = uint32_t;
using i64 = int64_t; using u64 = uint64_t;
using f32 = float_t; using f64 = double_t;
using usize = size_t;using str = string;
template <class T> using vec = vector<T>;
#define times(n, i) for (i32 i = 0; i < (n); i++)
#define range(n, m, i) for (i32 i = (n); i < (m); i++)
#define upto(n, m, i) for (i32 i = (n); i <= (m); i++)
#define downto(n, m, i) for (i32 i = (n); i >= (m); i--)
#define foreach(xs, x) for (auto &x : (xs))
#define all(xs) (xs).begin(), (xs).end()
#define sortall(xs) sort(all(xs))
#define reverseall(xs) reverse(all(xs))
#define uniqueall(xs) (xs).erase(unique(all(xs)), (xs).end())
#define maximum(xs) *max_element(all(xs))
#define minimum(xs) *min_element(all(xs))
const i64 MOD = 1000000007;

str solve(str s) {
    str ret;
    sortall(s);

    tuple<char, str, char> s1[5] = {
        make_tuple('Z', "ZERO", '0'),
        make_tuple('U', "FOUR", '4'),
        make_tuple('G', "EIGHT", '8'),
        make_tuple('X', "SIX", '6'),
        make_tuple('W', "TWO", '2'),
    };
    bool b = true;
    while (b) {
        b = false;
        times(5, i) {
            if (s.find(get<0>(s1[i])) != str::npos) {
                foreach(get<1>(s1[i]), ss) {
                    usize idx = s.find(ss);
                    s.erase(idx, 1);
                }
                ret += get<2>(s1[i]);
                b = true;
            }
        }
    }

    tuple<char, str, char> s2[4] = {
        make_tuple('F', "FIVE", '5'),
        make_tuple('O', "ONE", '1'),
        make_tuple('H', "THREE", '3'),
        make_tuple('S', "SEVEN", '7'),
    };
    b = true;
    while (b) {
        b = false;
        times(4, i) {
            if (s.find(get<0>(s2[i])) != str::npos) {
                foreach(get<1>(s2[i]), ss) {
                    usize idx = s.find(ss);
                    s.erase(idx, 1);
                }
                ret += get<2>(s2[i]);
                b = true;
            }
        }
    }

    while (s.find('I') != str::npos) {
        s.erase(s.find('I'), 1);
        ret += '9';
    }

    sortall(ret);
    return ret;
}

i32 main()
{
    i32 t;
    cin >> t;
    vec<str> s(t);
    times(t, i) {
        cin >> s[i];
    }
    times(t, i) {
        str ans = solve(s[i]);
        cout << "Case #" << (i+1) << ": " << ans << endl;
    }
    return 0;
}