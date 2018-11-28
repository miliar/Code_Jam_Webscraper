#include <bits/stdc++.h>

using namespace std;

const int N = 100;
int tests;
int n, m;
int a[N][N];
bool has_ans;

void input_data(){
    has_ans = true;
    cin >> n >> m;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) a[i][j] = 0;
}

long long f[N];

long long get_cnt(int n){
    long long c = (long long)(n - 2);
    c = max(0LL, c);
    return (1LL << c);
}

void solve(){
    long long cnt = get_cnt(n);
    if (m > cnt){
        has_ans = false;
        return;
    }
    for (int i = 0; i < n - 1; ++i)
        for (int j = i + 1; j < n; ++j) a[i][j] = 1;

    long long pw = (1LL << max(((long long)n - 3LL), 0LL));
    int v = n - 2;

    while (cnt > m){
        if (cnt - pw >= m){
            cnt -= pw;
            a[v][n - 1] = 0;
        }
        if (cnt == m) return;
        if (cnt - 1 == m && v != 0){
            a[0][n-1] = 0;
            return ;
        }
        v--;
        pw /= 2LL;
    }
}


void output_data(int test){
//    cerr << test << " done" << endl;
    cout << "Case #" << test << ": ";
    if (!has_ans){
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << "POSSIBLE" << endl;
        for (int i = 0; i < n; ++i, cout << endl)
            for (int j = 0; j < n; ++j) cout << a[i][j];
    }
}

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    f[0] = -1;
    cin >> tests;
    for (int test = 1; test <= tests; ++test){
        input_data();
        solve();
        output_data(test);
    }
    return 0;
}
