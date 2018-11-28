#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define all(a) begin(a),end(a)
#define sz(a) ((int)((a).size()))

const double bin_eps = 1e-11;
const double eps = 1e-12;

struct Entry {
    double rate;
    double temp;
};

struct Bucket {
    double vol;
    double temp;
};

void solve_case();
bool test(const vector<Entry> &data, double lim);
bool test2(vector<Bucket> buckets);

int main() {
    int num_case;
    scanf("%d", &num_case);
    for (int case_id = 1; case_id <= num_case; case_id++) {
        printf("Case #%d: ", case_id);
        solve_case();
    }
}

void solve_case() {
    int n;
    double tot_vol, tot_temp;
    scanf("%d%lf%lf", &n, &tot_vol, &tot_temp);
    vector<Entry> data(n);
    for (Entry &e: data)
        scanf("%lf%lf", &e.rate, &e.temp);
    sort(all(data), [](Entry a, Entry b) { return a.temp < b.temp; });
    if (data.front().temp > tot_temp || data.back().temp < tot_temp) {
        printf("IMPOSSIBLE\n");
        return;
    }

    for (Entry &e: data)
        e.temp -= tot_temp;

    double lo, hi;
    lo = 0.0;
    hi = 1000000000.0;
    while (hi - lo > bin_eps) {
        double mid = (lo + hi) / 2.0;
        //printf("test(%lf)\n", mid);
        if (test(data, mid))
            hi = mid;
        else
            lo = mid;
    }
    double ans = lo * tot_vol;
    printf("%.9lf\n", ans);
}

bool test(const vector<Entry> &data, double lim) {
    int n = sz(data);

    vector<double> vol_lim(n);
    for (int i=0; i<n; i++)
        vol_lim[i] = min(1.0, lim * data[i].rate);

    double vol_extra = -1.0;
    for (int i=0; i<n; i++)
        vol_extra += vol_lim[i];
    if (vol_extra < 0.0)
        return false;

    vector<Bucket> buckets(n);
    for (int i=0; i<n; i++) {
        buckets[i].vol = vol_lim[i];
        buckets[i].temp = data[i].temp;
    }
    if (!test2(buckets))
        return false;
    for (Bucket &b: buckets)
        b.temp = -b.temp;
    if (!test2(buckets))
        return false;
    return true;

    /*
    double curr_temp = 0.0;
    for (int i=0; i<n; i++)
        curr_temp += data[i].temp * vol_lim[i];

    if (curr_temp > 0.0 + eps) {
        for (int i=0; i<n; i++) {
            if (data[i].temp > 0.0 + eps)
                return false;
            double must_reduce = curr_temp / data[i].temp;
            //printf("must_reduce: %lf\n", must_reduce);
            if (must_reduce < vol_lim[i] + eps)
                return true;
            curr_temp -= data[i].temp * vol_lim[i];
            vol_lim[i] = 0.0;
        }
        return false;
    } else if (curr_temp < 0.0 - eps) {
        for (int i=n-1; i>=0; i--) {
            if (data[i].temp < 0.0 - eps)
                return false;
            double must_reduce = curr_temp / data[i].temp;
            //printf("must_reduce: %lf\n", must_reduce);
            if (must_reduce < vol_lim[i] + eps)
                return true;
            curr_temp -= data[i].temp * vol_lim[i];
            vol_lim[i] = 0.0;
        }
        return false;
    } else {
        return true;
    }
    */
}

bool test2(vector<Bucket> buckets) {
    int n = sz(buckets);
    sort(all(buckets), [](Bucket a, Bucket b) { return a.temp < b.temp; });
    double curr_temp = 0.0;
    double curr_remain = 1.0;
    for (int i=0; i<n && curr_remain > 0.0 + eps; i++) {
        Bucket &a = buckets[i];
        double add_vol = min(a.vol, curr_remain);
        a.vol -= add_vol;
        curr_remain -= add_vol;
        curr_temp += a.temp * add_vol;
    }
    return curr_temp < 0.0 + eps;
}
