#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

vector <string> v; 

//x = min_idx_gte(a); y = max_idx_lte(b);
int cmp(string a, string b)
{
    //1: a > b, 0: a = b, -1: a < b
    int i, len;
    if (a.length() > b.length()) return 1;
    if (a.length() < b.length()) return -1;
    len = a.length();
    for (i = 0; i < len; i++)
    {
        if (a[i] > b[i]) return 1;
        if (a[i] < b[i]) return -1;
    }
    return 0;
}

int min_idx_gte(string x)
{
    int a = 0, b = 41550, c, d;
    if (cmp(x, v[a]) == -1) return a;
    if (cmp(x, v[b]) == 1) return b + 1;
    while (1)
    {
        if (!cmp(x, v[a])) return a;
        if (!cmp(x, v[b])) return b;
        if ((b - a) <= 1) return b;
        c = (a + b) / 2; d = cmp(x, v[c]);
        if (!d) return c;
        if (d == 1) a = c;
        if (d == -1) b = c;
    }
}

int max_idx_lte(string x)
{
    int a = 0, b = 41550, c, d;
    if (cmp(x, v[a]) == -1) return -1;
    if (cmp(x, v[b]) == 1) return b;
    while (1)
    {
        if (!cmp(x, v[a])) return a;
        if (!cmp(x, v[b])) return b;
        if ((b - a) <= 1) return a;
        c = (a + b) / 2; d = cmp(x, v[c]);
        if (!d) return c;
        if (d == 1) a = c;
        if (d == -1) b = c;
    }
}

int main()
{
    int cnt, i, n, t, x, y;
    string a, b;
    v.resize(41551);
    /* here follows initialization for v[0] to v[41550], as pre-calculated using the following code: (the initialization omitted here due to size)
        #include <iostream>
        #include <string>
        #include <vector>
        #include <set>
        #include <map>
        #include <algorithm>
        
        using namespace std;
        
        int display(vector <int> a, vector <int> b)
        {
            int a1 = a.size(), b1 = b.size(), i;
            for (i = a1 - 1; i >= 0; i--) cout << a[i]; cout << "*";
            for (i = a1 - 1; i >= 0; i--) cout << a[i]; cout << "=";
            for (i = b1 - 1; i >= 0; i--) cout << b[i]; cout << endl;
        }
        
        bool is_fair(vector <int> x)
        {
            int i, len = x.size();
            for (i = 0; i <= (len / 2); i++) if (x[i] != x[len - i - 1]) return false;
            return true;
        }
        
        vector <int> square(vector <int> x)
        {
            int i, j, len = x.size(), len2;
            vector <int> y; len2 = (2 * len) - 1; y.resize(len2); for (i = 0; i < len2; i++) y[i] = 0;
            for (i = 0; i < len; i++) for (j = 0; j < len; j++) y[i + j] += (x[i] * x[j]);
            for (i = 0; i < (len2 - 1); i++) { if (y[i] >= 10) { y[i + 1] += (y[i] / 10); y[i] %= 10; } }
            return y;
        }
        
        int main()
        {
            int i, j, len, len1, len2, mod, n, temp, x;
            vector <int> a, b;
            freopen("test.txt", "w", stdout);
            //generate palindromes of each length (1 - 50) and check if their squares are palindromes too, according to the pattern
            cout << "1*1=1" << endl;
            cout << "2*2=4" << endl;
            cout << "2*3=9" << endl;
            for (len = 2; len <= 50; len++)
            {
                a.resize(len);
                len1 = len / 2; len2 = ((len % 2) ? (len1 + 1) : len1);
                n = 1;
                for (i = 1; i < len1; i++) n *= 2;
                if (len1 != len2) n *= 3;
                for (i = 0; i < n; i++)
                {
                    a[0] = 1; for (j = 1; j < len2; j++) a[j] = 0; x = len2 - 1;
                    mod = 2; if (len1 != len2) mod = 3;
                    temp = i; while (temp) { a[x] = temp % mod; temp /= mod; mod = 2; x--; }
                    for (j = 0; j < len1; j++) a[len - j - 1] = a[j];
                    b = square(a); if (is_fair(b)) display(a, b);
                }
                for (i = 0; i < len; i++) a[i] = 0; a[0] = 2; a[len - 1] = 2; b = square(a); if (is_fair(b)) display(a, b);
                if (len % 2) { a[len / 2] = 1; b = square(a); if (is_fair(b)) display(a, b); }
            }
            while(1);
            return 0;
        }
    */
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> a; cin >> b;
        x = min_idx_gte(a); y = max_idx_lte(b);
        n = y - x + 1; if (n < 0) n = 0;
        cout << "Case #" << cnt << ": " << n << endl;
    }
    return 0;
}
