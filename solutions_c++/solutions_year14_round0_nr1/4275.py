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

int A[17], B[17];

int main() {
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        int rsp1;
        scanf("%d", &rsp1);
        rep(i,4) rep(j,4) {
            int x;
            scanf("%d", &x);
            A[x] = i + 1;
        }
        int rsp2;
        scanf("%d", &rsp2);
        rep(i,4) rep(j,4) {
            int x;
            scanf("%d", &x);
            B[x] = i + 1;
        }
        int qtd = 0;
        int ans = -1;
        fr(i,1,17) if (A[i] == rsp1 and B[i] == rsp2) {
            ++qtd;
            ans = i;
        }
        printf("Case #%d: ", tc);
        if (qtd == 0) printf("Volunteer cheated!\n");
        else if (qtd > 1) printf("Bad magician!\n");
        else printf("%d\n", ans);
    }
    return 0;
}
