#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

using namespace std;

int mul(int a, int b) { // 1 = 1, i = 2, j = 3, k = 4
    int a1 = a, b1 = b, res = 0;
    if (a1 < 0) a1 = -a1;
    if (b1 < 0) b1 = -b1;
    if ((a1 == 1) || (b1 == 1)) res = a1 * b1;
    if ((a1 > 1) && (a1 == b1)) res = -1;
    if ((a1 == 2) && (b1 == 3)) res = 4;
    if ((a1 == 2) && (b1 == 4)) res = -3;
    if ((a1 == 3) && (b1 == 2)) res = -4;
    if ((a1 == 3) && (b1 == 4)) res = 2;
    if ((a1 == 4) && (b1 == 2)) res = 3;
    if ((a1 == 4) && (b1 == 3)) res = -2;
    if (a < 0) res = -res;
    if (b < 0) res = -res;
    return res;
}

int main()
{
    bool ok;
    int cnt, i, j, k, l, len, n1_i, n1_j, n1_k, q, t, x;
    string s, ss;
    vector <int> mul_pre, mul_post, n_i, n_j, n_k;
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> l; cin >> x;
        cin >> s;
        ss = ""; for (i = 0; i < x; i++) ss += s;

        len = l * x; mul_pre.resize(len); mul_post.resize(len);
        q = 1; for (i = 0; i < len; i++) { q = mul(q, ss[i] - 'g'); mul_pre[i] = q; }
        q = 1; for (i = len - 1; i >= 0; i--) { q = mul(ss[i] - 'g', q); mul_post[i] = q; }
        n1_i = 0; n1_j = 0; n1_k = 0;
        n_i.resize(len); n_j.resize(len); n_k.resize(len);
        for (i = 0; i < len; i++) {
            if (ss[i] == 'i') n1_i++;
            if (ss[i] == 'j') n1_j++;
            if (ss[i] == 'k') n1_k++;
            n_i[i] = n1_i; n_j[i] = n1_j; n_k[i] = n1_k;
        }

        ok = false;
        for (i = 0; i < len; i++) {
            if (mul_pre[i] == 2) {
                for (j = i + 2; j < len; j++) {
                    if (mul_post[j] == 4) {
                        n1_i = n_i[j - 1] - n_i[i]; n1_j = n_j[j - 1] - n_j[i]; n1_k = n_k[j - 1] - n_k[i];
                        n1_i %= 2; n1_j %= 2; n1_k %= 2;
                        if ((n1_i && (!n1_j) && n1_k) || ((!n1_i) && n1_j && (!n1_k))) {
                            //q = 1; for (k = i + 1; k < j; k++) q = mul(q, ss[k] - 'g');
                            //if (q == 3) { ok = true; break; }
                            if ((mul_pre[i] > 0) && (mul_pre[j - 1] > 0)) ok = true;
                            if ((mul_pre[i] < 0) && (mul_pre[j - 1] < 0)) ok = true;
                            if (ok) break;
                        }
                    }
                }
                if (ok) break;
            }
        }

        //display results
        cout << "Case #" << cnt << ": " << (ok ? "YES" : "NO") << endl;
    }
    return 0;
}
