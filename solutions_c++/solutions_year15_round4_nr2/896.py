#include <bits/stdc++.h>

using namespace std;

const long double eps = 1e-17;

bool my_less (const long double &a, const long double &b) {
    return a + eps < b;
}

bool my_gr (const long double &a, const long double &b) {
    return my_less(b, a);
}

bool my_eq (const long double &a, const long double &b) {
    return !(my_less(a, b) || my_less(b, a));
}

bool my_less_or_eq (const long double &a, const long double &b) {
    return !my_less(b, a);
}

bool my_gr_or_eq (const long double &a, const long double &b) {
    return !my_less(a, b);
}

struct Source {
    long double temperature, rate;

    bool operator < (const Source &other) const {
        if (temperature < other.temperature) return true;
        if (temperature > other.temperature) return false;
        return rate < other.rate;
    }
};

bool check (long double max_a, const long double &tot_v, const long double &tot_t, const vector<Source> &sources) {
    int n = sources.size();
    max_a /= tot_v;
    long double min_t = 0.0, max_t = 0.0;
    long double sum_a = 1.0;
    for (int i = 0; i < n; ++i) {
        long double cur_a = min(max_a * sources[i].rate, sum_a);
        sum_a -= cur_a;
        min_t += cur_a * sources[i].temperature;
    }
    if (!my_eq(sum_a, 0.0)) return false;
    sum_a = 1.0;
    for (int i = n - 1; i >= 0; --i) {
        long double cur_a = min(max_a * sources[i].rate, sum_a);
        sum_a -= cur_a;
        max_t += cur_a * sources[i].temperature;
    }
    if (!my_eq(sum_a, 0.0)) return false;
    //printf("%.7Lf %.7Lf\n", min_t, max_t);
    return my_less_or_eq(min_t, tot_t) && my_gr_or_eq(max_t, tot_t);
}

void Solve (int test_num) {
    int n;
    long double V, X;
    long double left = 0.0, right = 100000000;
    scanf("%d%Lf%Lf", &n, &V, &X);
    vector<Source> sources(n);
    for (int i = 0; i < n; ++i) {
        scanf("%Lf%Lf", &sources[i].rate, &sources[i].temperature);
        right = max(right, V / sources[i].rate);
    }
    sort(sources.begin(), sources.end());
    if (my_gr(sources[0].temperature, X) || my_less(sources[n - 1].temperature, X)) {
        printf("Case #%d: IMPOSSIBLE\n", test_num);
        return;
    }
    for (int i = 0; i < 200; ++i) {
        long double temp = (left + right) / 2.0;
        if (check(temp, V, X, sources)) {
            right = temp;
        } else {
            left = temp;
        }
    }
    printf("Case #%d: %.8Lf\n", test_num, right);
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        Solve(i + 1);
    }
}
