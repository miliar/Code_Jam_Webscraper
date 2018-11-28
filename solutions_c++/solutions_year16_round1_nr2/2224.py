#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<vector<int> > vvi;
int g[55][55], n, ans = 0;
bool dfs(int idx, int nr, int nc, int uk){
    int i, j;
    //printf("%d r:%d c:%d %d\n",idx,nr,nc,uk);
    //for(i=0;i<n;i++){
    //    for(j=0;j<n;j++)printf("%d ",g[i][j]);
    //    printf("\n");
    //}
    if(nr == n && nc == n){
        ans = uk;
        return true;
    }
    int ori[55];
    bool ok, done = false;
    //try row
    if(nr < n){
        if(idx < 2*n-1){
            ok = true;
            for(i=0;i<n;i++){
                if(g[nr][i] > 0 && g[nr][i] != vvi[idx][i]){
                    ok = false;
                    break;
                }
            }
            if(ok){
                for(i=0;i<n;i++){
                    ori[i] = g[nr][i];
                    g[nr][i] = vvi[idx][i];
                }
                if(!dfs(idx+1, nr+1, nc, uk)){
                    for(i=0;i<n;i++)
                        g[nr][i] = ori[i];
                }else
                    return true;
            }
        }
        if(uk == 0){
            if(dfs(idx, nr+1, nc, nr))
                return true;
        }
    }
    //try col
    if(nc < n){
        if(idx < 2*n - 1){
            ok = true;
            for(i=0;i<n;i++){
                if(g[i][nc] > 0 && g[i][nc] != vvi[idx][i]){
                    ok = false;
                    break;
                }
            }
            if(ok){
                for(i=0;i<n;i++){
                    ori[i] = g[i][nc];
                    g[i][nc] = vvi[idx][i];
                }
                if(!dfs(idx+1, nr, nc+1, uk)){
                    for(i=0;i<n;i++)
                        g[i][nc] = ori[i];
                }else
                    return true;
            }
        }
        if(uk == 0){
            if(dfs(idx, nr, nc+1, -nc))
                return true;
        }
    }
    return false;
}
int main()
{
    int tn, i, j;
    freopen("gcbs.in", "r", stdin);
    freopen("gcbs.out", "w", stdout);
    scanf("%d", &tn);
    for(int tt = 1; tt<=tn;tt++){
        scanf("%d", &n);
        vvi.clear();
        for(i=0;i<n*2-1;i++){
            vector<int> tmp;
            for(j=0;j<n;j++){
                int d;
                scanf("%d",&d);
                tmp.push_back(d);
            }
            vvi.push_back(tmp);
        }
        sort(vvi.begin(),vvi.end());
        //for(i=0;i<2*n-1;i++){
        //    for(j=0;j<n;j++)printf("%d ",vvi[i][j]);printf("\n");
        //}
        //special check
        if(vvi[0][0] != vvi[1][0]){
            int has[2505];
            memset(has,0,sizeof(has));
            for(i=0;i<2*n-1;i++)
                has[vvi[i][0]]++;
            for(i=0;i<n;i++)
                has[vvi[0][i]]--;
            printf("Case #%d: %d",tt,vvi[0][0]);
            for(i=0;i<=2500;i++)
                if(has[i])
                    printf(" %d",i);
            printf("\n");
        }else{
            for(i=0;i<n;i++)for(j=0;j<n;j++)
                g[i][j] = 0;
            for(i=0;i<n;i++){
                g[0][i] = vvi[0][i];
                g[i][0] = vvi[1][i];
            }
            dfs(2, 1, 1, 0);
            printf("Case #%d:",tt);
            if(ans > 0){
                for(i=0;i<n;i++)
                    printf(" %d",g[ans][i]);
            }else{
                for(i=0;i<n;i++)
                    printf(" %d",g[i][-ans]);
            }
            printf("\n");
        }
    }
}
