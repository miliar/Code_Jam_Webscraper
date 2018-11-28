#include<cstdio>
#include<cstring>
#define mod 1000000007
typedef long long ll;
int t, ct, n, m, ans, cnt;
char s[10][110];
int mk[10];
bool f[10];
struct Trie{
    int ch[1000][26];
    int sz;
    void init(){
        memset(ch[0],0,sizeof(ch[0]));
        sz=1;
    }
    int idx(char ch){
        return ch-'A';
    }
    void insert(char *ss){
        int u=0;
        int len = strlen(ss);
        for(int i=0; i<len; i++){
            int c = idx(ss[i]);
            if(!ch[u][c]){
                memset(ch[sz],0,sizeof(ch[sz]));
                ch[u][c]=sz++;
            }
            u = ch[u][c];
        }
    }
}tr[10];
int solve(){
    for(int i=0; i<m; i++){
        tr[i].init();
    }
    for(int i=0; i<n; i++){
        tr[mk[i]].insert(s[i]);
    }
    int res=0;
    for(int i=0; i<m; i++){
        res += tr[i].sz;
    }
    return res;
}
void dfs(int x){
    if(x==n){
        memset(f,0,sizeof(f));
        for(int i=0; i<n; i++){
            f[mk[i]]=1;
        }
        for(int i=0; i<m; i++){
            if(!f[i])   return;
        }
        int res = solve();
        if(res>ans){
            ans = res;
            cnt = 1;
        }
        else if(res==ans){
            cnt++;
        }
        return;
    }
    for(int i=0; i<m; i++){
        mk[x]=i;
        dfs(x+1);
    }
}
int main(){
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    scanf("%d",&t);
    for(ct=1; ct<=t; ct++){
        scanf("%d %d", &n, &m);
        for(int i=0; i<n; i++)  scanf("%s", s[i]);
        ans = cnt = 0;
        for(int i=0; i<m; i++){
            mk[0]=i;
            dfs(1);
        }
        printf("Case #%d: %d %d\n", ct, ans, cnt);
    }
    return 0;
}
