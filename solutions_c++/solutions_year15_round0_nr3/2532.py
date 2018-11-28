#include <cstdio>
#include <vector>
#include <cassert>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;

enum quat_inner
    {
        ONE = 1, I, J, K
    };

vector <vector <int> > mul_table =
    { { 0, 0, 0, 0 },
      { 0, 1, I, J, K },
      { 0, I, -1, K, -J },
      { 0, J, -K, -1, I },
      { 0, K, J, -I, -1}
    };

struct quat
{
    int value;

    quat() : value(1) {}
    quat(int value) : value(value) {}

    quat operator*(quat const& rhs) const
    {
        int value = this->value;
        bool sign = value < 0;
        sign ^= rhs.value < 0;
        value = abs(value);
        int rvalue = abs(rhs.value);
        int result = mul_table[value][rvalue];
        return quat{ sign ? -result : result };  
    }

    quat operator*=(quat const& rhs)
    {
        return *this = *this * rhs;
    }

    bool operator==(quat_inner const& o) const
    {
        return value == o;
    }
};

quat parse_quat(char c)
{
    switch (c) {
    case 'i': return I;
    case 'j': return J;
    case 'k': return K;
    }
    assert(false);
    return 1;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int te;
    cin >> te;

    vector <pair <int, int> > ans;
    for (int t = 1; t <= te; t++) {
        int l, x;
        cin >> l >> x;
        string s;
        cin >> s;

        int n = l * x;

        vector <quat> a(n);
        vector <quat> suf(n);
        for (int j = 0; j < x; j++) {
            for (int i = 0; i < l; i++) {
                a[j * l + i] = parse_quat(s[i]);
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            quat q = 1;
            if (i < n - 1) q = suf[i + 1];
            suf[i] = a[i] * q; 
        }

        quat aa = a[0];
        for (int left = 1; left < n; left++) {
            quat bb = a[left];
            for (int mid = left + 1; mid < n; mid++) {
                quat cc = suf[mid];
                if (aa == I && bb == J && cc == K) {
                    ans.push_back({t, 1});
                    goto END;
                }
                bb *= a[mid];
            }
            aa *= a[left];
        }

        ans.push_back({t, 0});
    END: assert(true);
    }

    sort(ans.begin(), ans.end());
    for (auto x : ans) {
        cout << "Case #" << x.first << ": " << (x.second ? "YES\n" : "NO\n");
    }

    return 0;
}
