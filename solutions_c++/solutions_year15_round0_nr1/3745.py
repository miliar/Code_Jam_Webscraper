#include <bits/stdc++.h>
#define fr(i,a,b) for(int i = (a), __ = (b); i < __; ++i)
#define frr(i,a,b) for(int i = (a), __ = (b); i >= __; --i)
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define cl(a,b) memset(a, b, sizeof a)
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d %d", &a, &b)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

int main(){
    int T; scanf("%d", &T);
    for(int cases = 1; cases <= T; ++cases) {
        int Smax; scanf("%d", &Smax);
        int resp = 0, qtdStood;
        scanf("%1d", &qtdStood);
        int k = 1;
        while(Smax--) {
            int nxt; scanf("%1d", &nxt);
            int need = max(k-qtdStood,0);
            resp += need;
            qtdStood += need+nxt;
            k++;
        }
        printf("Case #%d: %d\n", cases, resp);
    }
    return 0;
}

