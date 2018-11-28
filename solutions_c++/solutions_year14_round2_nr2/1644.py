#include <bits/stdc++.h>
#define fr(i,a,b) for (int i = (a), __ = (b); i < __; ++i)	
#define st first
#define nd second
#define dbg(x) cout << #x << " " << x << endl
using namespace std;

const double eps = 1e-7;
const int inf = 0x3f3f3f3f;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<int> vi;

int main() {
    int nt; scanf("%d", &nt); ++nt;
    fr(_,1,nt) {
        int a, b, k; scanf("%d %d %d", &a, &b, &k);
        int ans = 0;
        fr(i,0,a) fr(j,0,b) if ((i&j) < k) ++ans;
        printf("Case #%d: %d\n", _, ans);
    }
    return 0;
}
