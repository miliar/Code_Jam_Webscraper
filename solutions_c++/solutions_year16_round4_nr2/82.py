#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
template <class T> int size(const T &x) { return x.size(); }
const int INF = 2147483647;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

vector<double> cur;
map<ii,double> mem;
double prob(int at, int want) {
    if (at == size(cur)) {
        return want == 0 ? 1.0 : 0.0;
    }
    if (want < 0) {
        return 0.0;
    }
    ii st(at,want);
    if (mem.find(st) != mem.end())
        return mem[st];
    return mem[st] = cur[at] * prob(at+1, want-1) + (1-cur[at]) * prob(at+1,want);
}

int main() {
    int ts;
    scanf("%d", &ts);
    rep(t,0,ts) {
        printf("Case #%d: ", t+1);
        int n, k;
        scanf("%d %d", &n, &k);
        vector<double> arr(n);
        rep(i,0,n) scanf("%lf", &arr[i]);
        double mx = 0;
        sort(arr.begin(), arr.end());
        rep(start,0,2*n) {
            cur.clear();
            rep(i,0,k) {
                cur.push_back(arr[(i+start)%n]);
            }
            mem.clear();
            mx = max(mx, prob(0, k/2));
        }
        printf("%0.10lf\n", mx);
    }
    return 0;
}

