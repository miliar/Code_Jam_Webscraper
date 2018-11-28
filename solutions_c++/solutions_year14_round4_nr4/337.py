#include <bits/stdc++.h>
using namespace std;

struct trie
{
    trie *next[26];
}e[10010];

int cnt;
trie *root;

void init()
{
    
    root = NULL;
    for(int i = 0; i < cnt; i ++) {
        for(int j = 0; j < 26; j ++) {
            e[i].next[j] = NULL;
        }
    }
    cnt = 0;
}
    
void insert(char *s)
{
    if(!root) root = &e[cnt ++];
    trie *p = root;
    for(int i = 0,idx; s[i]; i ++) {
        idx = s[i] - 'A';
        if(!p->next[idx]) p->next[idx] = &e[cnt ++];
        p = p->next[idx];
    }
}

char s[110][110];
int n,m;
    
void solve()
{
    scanf("%d%d",&n,&m);
    for(int i = 0; i < n; i ++) scanf("%s",s[i]);
    int mul = 1;
    for(int i = 1; i <= n; i ++) mul *= m;
    int ans = 0,cc = 0;
    for(int i = 0; i < mul; i ++) {
        vector<int> v[10];
        int x = i;
        int sum = 0;
        for(int j = 0; j < n; j ++) {
            v[x % m].push_back(j);
            x /= m;
        }
        int tot = 0;
        for(int j = 0; j < m; j ++)
            if(v[j].size()) tot ++;
        if(tot != m) continue;
        for(int j = 0; j < m; j ++) {
            for(int k = 0; k < v[j].size(); k ++) {
                insert(s[v[j][k]]);
            }
            sum += cnt;
            init();
        }
        if(sum == ans) cc ++;
        else if(sum > ans) ans = sum,cc = 1;
    }
    cout << ans << " " << cc << endl;
}
    
int main() {    
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
