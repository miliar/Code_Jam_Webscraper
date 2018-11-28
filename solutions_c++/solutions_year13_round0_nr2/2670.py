#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

// #include <wara_lib.cc>
// #include <wara_list.cc>
// #include <wara_hash.cc>

typedef unsigned long long u_longlong;
typedef unsigned long u_long;
typedef unsigned char u_char;

// #define DEBUG
#define HASH_LEN 256

int calc2(vector< vector<long> > vc, long index, long n, long m, vector<long> ns, vector<long> ms);

int calc3(vector< vector<long> > vc, long index, long n, long m, vector<long> ns, vector<long> ms)
{
    long i;
    long a;

#ifdef DEBUG
    cout << "calc3(): " << index << endl;
#endif /* DEBUG */
    if (ms[index] == 1) {
        return (0);
    }
    if (ms[index] == 2) {
        return (1);
    }

#ifdef DEBUG
    // cout << "calc3(): for run." << endl;
#endif /* DEBUG */
    a = vc[0][index];
    for (i = 1; i < n; i++) {
        if (a > vc[i][index]) {
            ms[index] = 1;
            if (!calc2(vc, i, n, m, ns, ms)) {
                return (0);
            }
        } else if (a < vc[i][index]) {
            long j;

            ms[index] = 1;
            for (j = 0; j < n; j++) {
                if (vc[i][index] > vc[j][index]) {
                    if (!calc2(vc, j, n, m, ns, ms)) {
                        return (0);
                    }
                }
            }
        }
    }

    ms[index] = 2;

    return (1);
}

int calc2(vector< vector<long> > vc, long index, long n, long m, vector<long> ns, vector<long> ms)
{
    long i;
    long a;

#ifdef DEBUG
    cout << "calc2(): " << index << endl;
#endif /* DEBUG */
    if (ns[index] == 1) {
        return (0);
    }
    if (ns[index] == 2) {
        return (1);
    }

#ifdef DEBUG
    // cout << "calc2(): for run." << endl;
#endif /* DEBUG */
    a = vc[index][0];
    for (i = 1; i < m; i++) {
        if (a > vc[index][i]) {
            ns[index] = 1;
            if (!calc3(vc, i, n, m, ns, ms)) {
                return (0);
            }
        } else if (a < vc[index][i]) {
            long j;

            ns[index] = 1;
            for (j = 0; j < m; j++) {
                if (vc[index][i] > vc[index][j]) {
                    if (!calc3(vc, j, n, m, ns, ms)) {
                        return (0);
                    }
                }
            }
        }
    }

    ns[index] = 2;

    return (1);
}

const char *calc(vector< vector<long> > vc, long n, long m)
{
    vector<long> ns, ms;
    long i;

    ns.resize(n);
    for (i = 0; i < n; i++) {
        ns[i] = 0;
    }
    ms.resize(m);
    for (i = 0; i < m; i++) {
        ms[i] = 0;
    }

    for (i = 0; i < n; i++) {
        if (!calc2(vc, i, n, m, ns, ms)) {
            return ("NO");
        }
    }

    return ("YES");
}

void exec(u_longlong num)
{
    const char *ans;
    vector< vector<long> > vc;
    long i, j, n, m;

    cin >> n >> m;
#ifdef DEBUG
    cout << n << ' ' << m << endl;
#endif /* DEBUG */
    vc.resize(n);
    for (i = 0; i < n; i++) {
        vc[i].resize(m);
        for (j = 0; j < m; j++) {
            cin >> vc[i][j];
        }
    }

#ifdef DEBUG
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            cout << vc[i][j] << ' ';
        }
        cout << endl;
    }
#endif /* DEBUG */

    ans = calc(vc, n, m);

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
    cout << "b_small start " << t << endl;
#endif /* DEBUG */
    for (i = 0; i < t; i++) {
        exec(i + 1);
    }

    return (0);
}
