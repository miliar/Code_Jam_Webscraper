#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

// #include <wara_lib.cc>
// #include <wara_list.cc>
// #include <wara_hash.cc>

typedef long long longlong;
typedef unsigned long long u_longlong;
typedef unsigned long u_long;
typedef unsigned char u_char;

// #define DEBUG
// #define TITLE "a_small"
#define TITLE "a_large"
#define HASH_LEN 256

// #define SMAX 6
#define SMAX 1000

// u_longlong calc(vector< vector<long> > vc, long n, long m)
u_longlong calc(vector< vector<long> > vc, char *c)
{
    u_longlong i, total, f;
    char *p;

#ifdef DEBUG
    // cout << "calc(): " << n << " " << m << endl;
    cout << "calc(): " << endl;
#endif /* DEBUG */

    total = 0;
    f = 0;
    p = c;
    for (i = 0; i <= vc[0][0]; i++) {
        u_longlong num;
        num = (u_longlong)(*p - '0');
#ifdef DEBUG
        cout << "num: " << num << endl;
#endif /* DEBUG */

        if (total < i) {
            f += i - total;
            total += i - total;
        }
        total += num;

        if (total >= SMAX) {
#ifdef DEBUG
        cout << "break" << endl;
#endif /* DEBUG */
            break;
        }

        p++;
    }

    return (f);
}

void exec(u_longlong num)
{
    u_longlong ans;
    // char *ans;
    vector< vector<long> > vc;
    long i, j, n, m;
    char c[1001 + 1];

#ifdef DEBUG
    cout << "exec(): " << num << endl;
#endif /* DEBUG */

    // cin >> n >> m;
    n = 1;
    m = 1;
#ifdef DEBUG
    cout << n << ' ' << m << endl;
#endif /* DEBUG */
    vc.resize(n);
    for (i = 0; i < n; i++) {
        vc[i].resize(m);
        for (j = 0; j < m; j++) {
            cin >> vc[i][j];
        }
        cin >> c;
    }

#ifdef DEBUG
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            cout << vc[i][j] << ' ';
        }
        cout << c << endl;
    }
#endif /* DEBUG */

    // ans = calc(vc, n, m);
    ans = calc(vc, c);

    cout << "Case #" << num << ": ";
    cout << ans;
    cout << endl;

    return;
}

int main(int argc, char **argv)
{
    u_longlong t, i;

    cin >> t;
#ifdef DEBUG
    cout << TITLE << " start " << t << endl;
#endif /* DEBUG */
    for (i = 0; i < t; i++) {
        exec(i + 1);
    }

    return (0);
}
