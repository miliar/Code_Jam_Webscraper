#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define F first
#define S second
#define pb push_back
#define rep(I,N) for(int (I) = 0; (I) < (N); (I)++)

typedef pair<int,int> pii;
typedef long long ll;
#define MAXN 107
char tab[MAXN][MAXN];
int rx[] = {0, 0, 1, -1};
int ry[] = {1,-1, 0, 0};
char arrows[] = {'v', '^', '>', '<'};
int r,c;
bool goUntil(pii p, int dir){
    if (p.F < 0 || p.F >= c || p.S < 0 || p.S >= r)
        return false;
    if (tab[p.F][p.S] != '.')
        return true;
    return goUntil(mp(p.F + rx[dir], p.S + ry[dir]), dir);
}
bool pointsto(pii x){
    if (tab[x.F][x.S] == '.')
        return true;
    int arrow = -1;
    rep(i, 4)
        if (tab[x.F][x.S] == arrows[i])
            arrow = i;
    return goUntil(mp(x.F + rx[arrow], x.S + ry[arrow]), arrow);
}
int main(){
    int t;
    scanf("%d",&t);
    rep(testId,t){
        printf("Case #%d: ", testId+1);
        scanf("%d%d",&r,&c);
        rep(y, r) rep(x, c){
            scanf(" %c", &tab[x][y]);
        }
        bool ans = true;
        int res = 0;
        rep(y, r) rep(x, c){
            if (!pointsto(mp(x,y))){
                res++;
                bool failed = true;
                rep(move, 4){
                    tab[x][y] = arrows[move];
                    if (pointsto(mp(x,y)))
                        failed = false;
                }
                if (failed){
                    ans = false;
                    break;
                }
            }
        }

        if (!ans) printf("IMPOSSIBLE\n");
        else printf("%d\n", res);

    }
}
