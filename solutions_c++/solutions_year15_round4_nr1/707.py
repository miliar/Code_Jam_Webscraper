#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#define INF 111111111

using namespace std;
char s[222][222];
int getx(char x){
    if (x == '>' || x == '<') return 0;
    if (x == '^') return -1;
    return 1;
}
int gety(char x){
    if (x == '^' || x == 'v') return 0;
    if (x == '<') return -1;
    return 1;
}
int v[222][222];
int main(){
    int T, cas = 0, i, j, n, m, k;
      freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--){
        scanf("%d%d", &n, &m);
        for(i = 0; i < n; i++)
            scanf("%s", s[i]);
        memset(v,0, sizeof(v));
        int ans = 0;
        printf("Case #%d: ", ++cas);
        int ok = 1;
        for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)if (s[i][j] != '.'){
            int f = 0;
            for(k = 0; k < n; k++)
                if (k != i && s[k][j] != '.') f = 1;
            for(k = 0; k < m; k++)
                if (k != j && s[i][k] != '.') f = 1;
            if (!f) ok = 0;
        }
        if  (!ok) puts("IMPOSSIBLE"); else{
            for(i = 0; i < n; i++)
                for(j = 0; j < m; j++)
            if (s[i][j] != '.' && !v[i][j]){
                int x, y;
                x = i, y = j;
                int px, py;
//                cout<<"st  "<<x<<"  "<<y<<endl;
                while(1){
                    if (s[x][y] != '.') v[x][y] = 1;
                    if (s[x][y] != '.') {px= getx(s[x][y]), py = gety(s[x][y]);}
                    x += px;
                    y += py;
//                    cout<<x<<"  "<<y<<endl;
                    if (x < 0 || x >= n || y < 0 || y >= m) {ans++;break;}
                    if (v[x][y]) {break;}
                }
            }
            printf("%d\n", ans);
        }
    }
    return 0;
}
