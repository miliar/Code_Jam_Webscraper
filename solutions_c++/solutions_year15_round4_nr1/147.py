#include <bits/stdc++.h>
char s[110][110];
bool isArrow(char ch)
{
        return ch=='^' || ch=='v' || ch=='<' || ch=='>';
}
void init()
{
        freopen("A-large.in","r", stdin);
        freopen("out.txt","w",stdout);
}
int main()
{
        init();
        int ca = 1;
        int t, n, m;
        scanf("%d", &t);
        while(t--) {
                scanf("%d%d", &n, &m);
                int ret = 0;
                for(int i = 0; i < n; i++) {
                        scanf("%s", s[i]);
                }
                printf("Case #%d: ", ca++);
                bool error = false;
                for(int i = 0; i < n; i++) {
                        for(int j = 0; j < m; j++) {
                                if(isArrow(s[i][j])) {
                                        bool flag = false;
                                        if(s[i][j]=='^') {
                                                for(int k = i - 1; k >= 0; k--) {
                                                        if(isArrow(s[k][j])) {
                                                                flag = true;
                                                        }
                                                }
                                        }
                                        if(s[i][j]=='<') {
                                                for(int k = j - 1; k >= 0; k--) {
                                                        if(isArrow(s[i][k])) {
                                                                flag = true;
                                                        }
                                                }
                                        }
                                        if(s[i][j]=='>') {
                                                for(int k = j + 1; k < m; k++) {
                                                        if(isArrow(s[i][k])) {
                                                                flag = true;
                                                        }
                                                }
                                        }
                                        if(s[i][j] == 'v') {
                                                for(int k = i + 1; k < n; k++) {
                                                        if(isArrow(s[k][j])) {
                                                                flag=true;
                                                        }
                                                }
                                        }
                                        if(!flag) {
                                                ret++;
                                                bool flag = false;
                                                for(int k = 0; k < m; k++) if(k != j){
                                                        if(isArrow(s[i][k])) {
                                                                flag = true;
                                                        }
                                                } 
                                                for(int k = 0; k < n; k++) if(k != i) {
                                                        if(isArrow(s[k][j])) {
                                                                flag = true;
                                                        }
                                                }
                                                if(!flag) {
                                                        error = true;
                                                }
                                        }
                                }
                        }
                }
                if(error) puts("IMPOSSIBLE");
                else 
                printf("%d\n", ret);
        }
        return 0;
}
