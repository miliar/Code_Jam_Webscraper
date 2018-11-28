#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

// #include <wara_lib.cc>
#include <wara_list.cc>
// #include <wara_hash.cc>

typedef long long longlong;
typedef unsigned long long u_longlong;
typedef unsigned long u_long;
typedef unsigned char u_char;

// #define DEBUG
#define TITLE "b_small"
// #define TITLE "b_large"
#define HASH_LEN 256

typedef struct {
    u_longlong cake;
    u_longlong plate;
} num_t;

void ana(wara_list_info_t *tbl, vector< vector<long> > vc, long m)
{
    long i;

    for (i = 0; i < m; i++) {
        num_t *data;
        long j, x;

        if (vc[0][i] == 0) {
            continue;
        }

        x = vc[0][i];

        data = (num_t *)malloc(sizeof(num_t));
        data->cake = x;
        data->plate = 0;
        wara_list_add_tail(tbl, data);

        for (j = 0; j < m; j++) {
            if (vc[0][j] == x) {
                (data->plate)++;
                vc[0][j] = 0;
            }
        }
    }
}

num_t *s_max(wara_list_info_t *tbl)
{
    num_t *data, *max;
    void *param;

    max = NULL;
    param = NULL;
    while ((data = (num_t *)wara_list_foreach(tbl, &param)) != NULL) {
        if (max == NULL) {
            max = data;
        } else {
            if (max->cake < data->cake) {
                max = data;
            }
        }
    }

    return (max);
}

void add(wara_list_info_t *tbl, u_longlong cake, u_longlong plate)
{
    num_t *data;
    void *param;

    param = NULL;
    while ((data = (num_t *)wara_list_foreach(tbl, &param)) != NULL) {
        if (data->cake == cake) {
            data->plate += plate;
            break;
        }
    }

    if (data == NULL) {
        num_t *data;

        data = (num_t *)malloc(sizeof(num_t));
        data->cake = cake;
        data->plate = plate;
        wara_list_add_tail(tbl, data);
    }

    return;
}

u_longlong divide(wara_list_info_t *tbl, num_t *target, int pattern)
{
    u_longlong time, a, b;

    if (pattern == 0 && target->cake == 9 && target->plate == 1) {
        time = 2;
        add(tbl, 3, 3);
    } else {
        time = target->plate;

        b = target->cake;
        a = (b + 1) / 2;
        b = b - a;

        add(tbl, a, target->plate);
        add(tbl, b, target->plate);
    }

    wara_list_detach(tbl, target);
    free((void *)target);

    return (time);
}

u_longlong calc2(wara_list_info_t *tbl, int pattern)
{
    u_longlong base, min;

    base = 0;
    min = 1000;
    while (1) {
        num_t *data;
        u_longlong time;

        data = s_max(tbl);
        time = base + data->cake;
#ifdef DEBUG
        cout << "--" << endl;
        cout << "min: " << min << " time: " << time << "(" << base << ")" << endl;
#endif /* DEBUG */
        if (min > time) {
            min = time;
        }

        if (data->cake <= 1) {
            break;
        }

        base += divide(tbl, data, pattern);

#ifdef DEBUG
        param = NULL;
        while ((data = (num_t *)wara_list_foreach(tbl, &param)) != NULL) {
            cout << "cake: " << data->cake << " plate: " << data->plate << endl;
        }
#endif /* DEBUG */
    }

    return (min);
}

u_longlong calc(vector< vector<long> > vc, long m)
// char *calc(vector< vector<long> > vc)
{
    wara_list_info_t tbl, tbl2;
    num_t *data;
    u_longlong t, min;
#ifdef DEBUG
    void *param;
#endif /* DEBUG */

#ifdef DEBUG
    cout << "calc(): " << m << endl;
    // cout << "calc(): "  << endl;
#endif /* DEBUG */

    wara_list_info_init(&tbl);
    ana(&tbl, vc, m);
#ifdef DEBUG
    param = NULL;
    while ((data = (num_t *)wara_list_foreach(&tbl, &param)) != NULL) {
        cout << "cake: " << data->cake << " plate: " << data->plate << endl;
    }
#endif /* DEBUG */


    wara_list_info_init(&tbl2);
    wara_list_dup(&tbl2, &tbl, sizeof(num_t));
    min = calc2(&tbl2, 0);
    while ((data = (num_t *)wara_list_remove(&tbl2, 0)) != NULL) {
        free((void *)data);
    }

    wara_list_info_init(&tbl2);
    wara_list_dup(&tbl2, &tbl, sizeof(num_t));
    t = calc2(&tbl2, 1);
    while ((data = (num_t *)wara_list_remove(&tbl2, 0)) != NULL) {
        free((void *)data);
    }
    if (min > t) {
        min = t;
    }

    return (min);
}

void exec(u_longlong num)
{
    u_longlong ans;
    // char *ans;
    vector< vector<long> > vc;
    long i, j, n, m;

#ifdef DEBUG
    cout << "exec(): " << num << endl;
#endif /* DEBUG */

    cin >> m;
    n = 1;
    // m = 0;
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

    ans = calc(vc, m);
    // ans = calc(vc);

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
