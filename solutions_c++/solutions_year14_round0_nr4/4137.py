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
        int N;
        scanf("%d", &N);
        vector<double> naomi(N), ken(N);
        
        for (double &x : naomi) scanf("%lf", &x);            
        for (double &x : ken) scanf("%lf", &x);
        
        sort(all(naomi));
        sort(all(ken));
        
        vector<int> used(N, 0);
        int rsp1 = 0, rsp2 = 0;
        rep(i,N) {
            double chosen_n = naomi[i];
            int id_k = -1;
            for (int j = 0; j < N; ++j) if (!used[j] and ken[j] > chosen_n) {
                id_k = j;
                break;
            }
            if (id_k == -1) {
                for (int j = 0; j < N; ++j) if (!used[j]) {
                    id_k = j;
                    break;
                }
            }
            used[id_k] = 1;
            double chosen_k = ken[id_k];
            if (chosen_n > chosen_k) ++rsp2;
        }
        int id = N - 1;
        for (int i = N - 1; i >= 0; --i) {
            if (naomi[id] > ken[i]) {
                ++rsp1;
                --id;
            }
        }
        printf("Case #%d: %d %d\n", tc, rsp1, rsp2);
    }
    return 0;
}
