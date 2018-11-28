#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = 222; 
const long long INF = 1e9 + 19;

int n, k;
double a[N];
double b[N];


void read() {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%lf", &a[i]);
}

void upd(double & a, double b) {
    a = max(a, b);
}

void calc(double * a, vector < vector < double > > & dp) {
    dp[0][0] = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j <= i; j++) {
            dp[i + 1][j] += dp[i][j] * (1 - a[i]);
            dp[i + 1][j + 1] += dp[i][j] * a[i];
        }
}

void solve() {
    sort(a, a + n);
    for (int i = 0; i < n; i++)
        b[i] = a[i];
    reverse(b, b + n);
    vector < vector < double > > dp1(n + 1, vector < double > (n + 1));
    vector < vector < double > > dp2(n + 1, vector < double > (n + 1));
    calc(a, dp1);
    calc(b, dp2);

    double answer = 0;
    for (int l = 0; l <= k; l++) {
        int r = k - l;
        double sum = 0;
        for (int j = 0; j <= k / 2; j++)        
            sum += dp1[l][j] * dp2[r][k / 2 - j];
        answer = max(answer, sum);
    }

    printf("%.17f\n", answer);




}

void stress() {

}


int main(){
#ifdef MY_DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            printf("Case #%d: ", tt + 1);
            read();
            solve();
        }
    }
    else {
        stress();
    }

    return 0;
}

