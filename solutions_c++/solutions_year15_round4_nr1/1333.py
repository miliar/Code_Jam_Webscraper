#include<bits/stdc++.h>
#define rep(i,k,n) for(int i= (int) k;i< (int) n;i++)
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
const long long inf = 9223372036854775807ll;
const int iinf = 2147483647;
const int limit = 1048576;
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w",stdout);
    int tes; scanf("%d", &tes);
    rep(t, 1, tes + 1){
        int r, c; scanf("%d%d", &r, &c);
        vector< vector<char> > grid(r + 1, vector<char>(c + 1));
        bool imp = false;

        rep(i, 1, r + 1)
            rep(j, 1, c + 1)
                scanf("\n%c", &grid[i][j]);

        int res = 0;
        rep(i, 1, r + 1)
            rep(j, 1, c + 1){
                if(grid[i][j] == '.')
                    continue;
                bool prob = true;

                rep(k, j, c + 1){
                    if(k > j && grid[i][k] != '.'){
                        prob = false;
                        break;
                    }
                    if(k == c && grid[i][j] == '>')
                        res++;
                }

                for(int k = j; k > 0; k--){
                    if(k < j && grid[i][k] != '.'){
                        prob = false;
                        break;
                    }
                    if(k == 1 && grid[i][j] == '<')
                        res++;
                }

                for(int k = i; k > 0; k--){
                    if(k < i && grid[k][j] != '.'){
                        prob = false;
                        break;
                    }
                    if(k == 1 && grid[i][j] == '^')
                        res++;
                }

                for(int k = i; k < r + 1; k++){
                    if(k > i && grid[k][j] != '.'){
                        prob = false;
                        break;
                    }
                    if(k == r && grid[i][j] == 'v')
                        res++;
                }

                if(prob)
                    imp = true;
            }

        if(imp)
            printf("Case #%d: IMPOSSIBLE\n", t);
        else
            printf("Case #%d: %d\n", t, res);
    }
    return 0;
}

