#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int T,M,N,tot,w[10],ans,ans1;
int ch[100][26];
string S[10];

void add(string st) {
    int len = st.length(),g = 0;
    for (int i = 0;i < len; i++) {
        int k = st[i]-'A';
        if (ch[g][k] == 0) {
                ch[g][k] = tot;
                memset(ch[tot],0,sizeof(ch[tot]));
                tot++;
        }
        g = ch[g][k];
    }
}

void dfs(int x) {
    if (x > M) {
        int tot1 = 0; bool flag = true;
        for (int k = 1;k <= N; k++) {
            tot = 1; memset(ch[0],0,sizeof(ch[0]));
            int sg = 0;
            for (int i = 1;i <= M; i++) {
                if (w[i] == k) {
                        add(S[i]);
                        sg++;
                }
            }
            if (sg == 0) {flag = false; break;}
            tot1 += tot;
        }
        if (flag) {
            if (tot1 > ans) { ans = tot1; ans1 = 1; }
            else if (tot1 == ans) ans1++;
        }
    }else {
        for (int i = 1;i <= N; i++) {
            w[x] = i;
            dfs(x+1);
        }
    }
}
int main() {
    #ifndef ONLINE_JUDGE
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&T);
    for (int kase = 1;kase <= T; kase++) {
        scanf("%d%d",&M,&N); w[0] = 0; ans = 0; ans1 = 1;
        for (int i = 1;i <= M; i++) cin>>S[i];
        dfs(1);
        printf("Case #%d: %d %d\n",kase,ans,ans1);
    }
    return 0;
}
