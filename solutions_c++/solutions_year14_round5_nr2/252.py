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

ll p, q, N;
vector<ll> H, G;

void input() {
    cin >> p >> q >> N;
    H = vector<ll>(N);
    G = vector<ll>(N);
    rep(i, N) {
        cin >> H[i] >> G[i];
    }
}

ll memo[100][1005];
bool vis[105][1005];

vector<ll> tower, player;

long long rec(int i, int turn) {
    long long ans = -(1LL << 40);
    
    if (turn > 1000) return -(1LL << 40);
    if (turn < 0) return -(1LL << 40);
    if (vis[i][turn]) return memo[i][turn];

    if (i == 0) return turn == 1 ? 0 : -(1LL << 40);
    ans = max(ans, rec(i, turn + 1));
    ans = max(ans, G[i-1] + rec(i-1, turn + player[i-1] - (tower[i-1] - 1))); 
    ans = max(ans, rec(i-1, turn - tower[i - 1]));
    //cerr << i << " " << turn << " " << ans << endl;
    vis[i][turn] = true;
    return memo[i][turn] = ans;
}

void solve() {
    tower = vector<ll>(N);
    player = vector<ll>(N);

    rep(i, N + 1)rep(j,1005) vis[i][j] = false;

    rep(i, N) {
        tower[i] = (H[i] + q - 1) / q;
        player[i] = (H[i] - q * (tower[i] - 1) + p - 1) / p;
        //cerr << tower[i] << " " << player[i] << endl;
    }

    cout << rec(N, 0) << endl;
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
