#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int T,N,ans;
char s[10][10];
int use[10],a[10],ma[10];
int dfs2(int dep)
{
    if(dep == N)
        return 1;
    int flag = 0;
    for(int i = 0; i < N; ++i) {
        if(s[a[dep]][i] == '1' && !ma[i]) {
            ma[i] = 1;
            flag = 1;
            if(!dfs2(dep + 1))
                return 0;
            ma[i] = 0;
        }
    }
    return flag;
}
int dfs1(int dep)
{
    if(dep == N) {
        /*printf("dfs2 \n");
        for(int i = 0; i < N; ++i)
            printf("%d ",a[i]);
        printf("\n");*/
        memset(ma,0,sizeof(ma));
        return dfs2(0);
    }
    for(int i = 0; i < N; ++i) {
        if(!use[i]) {
            use[i] = 1;
            a[dep] = i;
            if(!dfs1(dep + 1))
                return 0;
            use[i] = 0;
        }
    }
    return 1;
}
void dfs(int dep,int cost)
{
    if(dep == N * N) {
        memset(use,0,sizeof(use));
        if(dfs1(0)) {
            /*printf("### %d\n",cost);
            for(int i = 0; i < N; ++i)
                printf("@@@ %s\n",s[i]);*/
            ans = min(ans, cost);
        }
        return;
    }
    dfs(dep +1, cost);
    if(s[dep/N][dep%N] == '0') {
        s[dep/N][dep%N] = '1';
        dfs(dep + 1, cost + 1);
        s[dep/N][dep%N] = '0';
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int casei = 1; casei <= T; ++casei) {
        scanf("%d",&N);
        for(int i = 0; i < N; ++i)
            scanf("%s",s[i]);
        ans = 100;
        dfs(0,0);
        printf("Case #%d: %d\n",casei,ans);
    }
    return 0;
}
