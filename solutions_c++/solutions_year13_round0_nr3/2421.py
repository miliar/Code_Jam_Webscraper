#include <stdio.h>
#include <math.h>
#include <iostream>
#include <vector>
using namespace std;

#include <wara_list.cc>
// #include <wara_hash.cc>

unsigned long long wara_pow(unsigned long long x, unsigned long long y)
{
    unsigned long long i;
    unsigned long long ret = 1;

    if (y == 0) {
        return (ret);
    }

    for (i = 0; i < y; i++) {
        ret *= x;
    }

    return (ret);
}

typedef unsigned long long u_longlong;
typedef unsigned long u_long;

// #define DEBUG
#define HASH_LEN 256

wara_list_info_t info;

int check(u_longlong a)
{
    u_longlong x = 1, y, z1, z2;

    while (1) {
        y = a / x;
        if (y < 10) {
            break;
        }
        x *= 10;
    }

    y = 1;
    while (x > y) {
        z1 = (a / x) % 10;
        z2 = (a % (y * 10)) / y;
        if (z1 != z2) {
            return (0);
        }
        x /= 10;
        y *= 10;
    }

    return (1);
}

u_longlong calc(wara_list_info_t *info, u_longlong a, u_longlong b)
{
    u_longlong count;
    u_longlong *val;
    void *param = NULL;

    count = 0;
    while ((val = (u_longlong *)wara_list_foreach(info, &param)) != NULL) {
        if (*val >= a && *val <= b) {
            count++;
#ifdef DEBUG
            cout << (u_longlong)sqrt(*val) << "^2 = " << *val << endl;
#endif /* DEBUG */
        }
    }

    return (count);
}

void calc2(wara_list_info_t *info, u_longlong a, u_longlong b)
{
    u_longlong i, start, end;
    u_longlong val;

    start = (u_longlong)sqrt((double)a);
    end = (u_longlong)sqrt((double)b);
#ifdef DEBUG
    cout << start << ' ' << end << endl;
#endif /* DEBUG */
    for (i = start; i <= end; i++) {
        if (check(i)) {
#ifdef DEBUG
            // cout << "check ok: " << i << endl;
#endif /* DEBUG */
            val = wara_pow(i, 2);
            if (  a <= val && val <= b
               && check(val)) {
                u_longlong *val2;
                val2 = (u_longlong *)malloc(sizeof(u_longlong));
                *val2 = val;
                wara_list_add_tail(info, val2);
#ifdef DEBUG
                cout << i << "^2=" << val << endl;
#endif /* DEBUG */
            }
        }
    }

    return;
}

void exec(u_longlong num)
{
    u_longlong ans, a, b;

    cin >> a >> b;
#ifdef DEBUG
    cout << a << ' ' << b << endl;
#endif /* DEBUG */

    ans = calc(&info, a, b);

    cout << "Case #" << num << ": ";
    cout << ans;
    cout << endl;

    return;
}

int main(int argc, char **argv)
{
    u_longlong t, i;

    wara_list_info_init(&info);
    calc2(&info, 1, 100000000000000);
#ifdef DEBUG
    cout << "count: " << wara_list_get_count(&info) << endl;
#endif /* DEBUG */

    cin >> t;
#ifdef DEBUG
    cout << "c_small start " << t << endl;
#endif /* DEBUG */
    for (i = 0; i < t; i++) {
        exec(i + 1);
    }

    return (0);
}
