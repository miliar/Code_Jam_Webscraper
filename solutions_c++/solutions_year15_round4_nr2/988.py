// Author: Nguyen Duy Khanh
#include<bits/stdc++.h>
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define DEBUG(x) { printf << #x << " = " << x << endl; }
#define DEBUGARR(a,n) {cout << #a << " = " ; FOR(_,1,n) cout << a[_] << ' '; cout <<endl;}
#define CHECK printf("OK\n");
#define FILL(a, b) memset((a), (b), sizeof((a)))
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define Nmax 35000
using namespace std;

double a[111], b[111], v, t, k, res;
int test, n;

double solve(int i, int j){
    if (b[i] > t && b[j] > t) return -1;
    if (b[i] < t && b[j] < t) return -1;

    double xx, yy;
    yy = v * (t - b[i]) / (a[j] * (b[j] - b[i]));
    xx = (v - a[j] * yy) / a[i];
    return max(xx, yy);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> test;
    FOR(o,1,test){
        scanf("%d %lf %lf", &n, &v, &t);
        FOR(i,1,n) scanf("%lf %lf", &a[i], &b[i]);
        res = 987654321987654321LL;
        FOR(i,1,n)
            if (b[i] == t) res = min(res, v / a[i]);
        if (n == 2)
            if (b[1] == t && b[2] == t) {
                a[1] = a[1] + a[2];
                n = 1;
            }
        if (n == 1){
            res = v / a[1];
            if (t != b[1]) printf("Case #%d: IMPOSSIBLE\n", o);
            else printf("Case #%d: %.6f\n", o, res);
        }
        else{
            res = solve(1,2);
            if (res == 987654321987654321LL || res < 0) printf("Case #%d: IMPOSSIBLE\n", o);
            else printf("Case #%d: %.6f\n", o, res);
        }
    }

    return 0;
}
