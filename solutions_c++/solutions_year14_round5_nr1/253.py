// bigint: -lgmpxx -lgmp
// parallel: -fopenmp
#include <bits/stdc++.h>
#include <gmpxx.h>
#include <omp.h>
#include <sys/time.h>

#define BEGIN struct Solver {
#define END };

#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

typedef long long ll;
typedef mpz_class bigint;

using namespace std;

void init() {
}

BEGIN  ///////////////////////

ll N, p, q, r, s;

void input() {
    cin >> N >> p >> q >> r >> s;
}

void solve() {
    vector<ll> arr(N), sum(N + 1);
    rep(i, N) {
        arr[i] = (i * p + q) % r + s;
    }
    rep(i, N) {
        sum[i + 1] = arr[i] + sum[i];
    }

    ll ans = 0;
    ll j = 0;
    rep(i, N) {
        ll left = sum[i];
        ll mid = sum[j + 1] - sum[i];
        ll right = sum[N] - sum[j + 1];
        while (j < N && mid != max(left, max(mid, right))) {
            ans = max(ans, sum[N] - max(left, max(mid, right)));
            j++;
            mid = sum[j + 1] - sum[i];
            right = sum[N] - sum[j + 1];
        }
        ans = max(ans, sum[N] - max(left, max(mid, right)));
    }
    cout << setprecision(20) << (double)ans / (double) sum[N] << endl;
}

//////////////////////////////

string output() {
    stringstream out;
    out << "Case #" << caseNum << ": ";
    out << cout.str();
    return out.str();
}

void stop() {
    cerr << "  Case " << caseNum << ": ";
    cerr << (int)((getTime() - startTime) * 1000) << " ms" << endl;
}

stringstream cout;
int caseNum;
double startTime;

double getTime() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + tv.tv_usec / 1.0e6;
}

Solver(int n) : caseNum(n) { startTime = getTime(); };

END  /////////////////////////

int main() {
    int k;
    cin >> k;
    vector<string> out(k);
    init();

#ifdef _OPENMP
    cerr << "*Parallel Mode" << endl;

    omp_lock_t lock;
    omp_init_lock(&lock);
    int id = 0;

#pragma omp parallel for
    rep(i, k) {
        int myId;
        omp_set_lock(&lock);
        myId = id;
        Solver s(++id);
        s.input();
        omp_unset_lock(&lock);
        s.solve();
        s.stop();
        out[myId] = s.output();
    }
    omp_destroy_lock(&lock);
#else
    cerr << "*Single Mode" << endl;

    rep(i, k) {
        Solver s(i + 1);
        s.input();
        s.solve();
        s.stop();
        out[i] = s.output();
    }
#endif
    rep(i, k) {
        cout << out[i];
    }
    return 0;
}
