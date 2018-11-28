#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int x[20], y[20], m = 0, ans, N;
bool vis[5];
bool vis1[5];
bool OK;
bool A[5][5];
void dfs2(int d) {
    if (d>N || !OK) return;
    for (int i = 1; i <= N; i++)
        if (!vis1[i]) {
        vis1[i] = true;
        bool find = false;
        for (int j = 1; j <= N; j++)
            if (!vis[j] && A[i][j]) {
                vis[j] = true;
                find = true;
                dfs2(d+1);
                vis[j] = false;
            }
        vis1[i] = false;
        if (!find) {OK = false; return;}
    }

}

bool check() {
    OK = true;

        memset(vis, 0, sizeof vis);
         memset(vis1, 0, sizeof vis1);
        dfs2(1);

    return OK;
}

void dfs(int i, int num) {
    if (i>m) {
        if (check()) {
            if(num<ans) {
                ans = num;
//                cout <<"get"<<ans<<endl;
//                for (int i = 1; i <= m; i++)
//                    if (A[x[i]][y[i]])
//                        cout << x[i] << " " << y[i]<<endl;
            }
        }
        return;
    }
    if (num>ans) return;
    A[x[i]][y[i]] = false;
    dfs(i+1,num);
    A[x[i]][y[i]] = true;
    dfs(i+1,num+1);
}


int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-s.out", "w", stdout);
    int testcase;
    cin >> testcase;
    for (int o = 1; o <= testcase; o++) {
        printf("Case #%d: ", o);
        cin >> N;
        string s;
        m = 0;
        for (int i = 1; i <= N; i++) {
            cin>>s;
            for (int j =1;j<=N; j++)
                if (s[j-1]=='1') {
                    A[i][j] = 1;
                }
                else{
                    A[i][j] = 0;
                    ++m;
                    x[m]=i,y[m]=j;
                }
        }
        ans = m;
        dfs(1,0);
        printf("%d\n",ans);
    }
}
