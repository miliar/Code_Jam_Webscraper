#include <bits/stdc++.h>
#define fr(i,a,b) for(int i = (a); i < (b); ++i)
#define rep(i,n) fr(i,0,n)
#define cl(a,b) memset((a), (b), sizeof(a))
#define all(c) (c).begin(), (c).end()
#define _ << ", " <<
#define db(x) cerr << #x " == " << x << endl

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long long ll;
const int inf = 0x3f3f3f3f;

int main() {
    //ios_base::sync_with_stdio(false);
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        int lim = (X + C - 1) / C;
        double ans = 1e10;
        double tempo = 0;
        double prod = 2;
        for (int i = 0; i <= lim; ++i) {
            ans = min(ans, tempo + X / prod);
            tempo += C / prod;
            prod += F;
        }
        printf("Case #%d: %.7lf\n", tc, ans);
    }
    return 0;
}
