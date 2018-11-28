#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
typedef pair<int,int> pi;
int TC, cm;
int N = 12;
pi comp[13][3];
int ord[13][3], tmp[3];
char buf[1000000], mp[] = "PRS";
int lol[13][3][3];
void recur(int n, int s){
    if(n == 0){
        buf[cm++] = mp[s];
        buf[cm] = 0;
    }
    else{
        recur(n-1, comp[n][s].first);
        recur(n-1, comp[n][s].second);
    }
}
int main(){
    scanf("%d", &TC);
    for(int i = 0; i < 3; ++i) ord[0][i] = i; //P, R, S
    for(int i = 1; i <= N; ++i){
        for(int s = 0; s < 3; ++s){
            if(ord[i-1][s] < ord[i-1][(s+1)%3]) comp[i][s] = pi(s, (s+1)%3);
            else comp[i][s] = pi((s+1)%3, s);
        }
        for(int j = 0; j < 3; ++j) tmp[j] = j;
        sort(tmp, tmp+3, [i](int a, int b){
            if(comp[i][a].first == comp[i][b].first) return ord[i-1][comp[i][a].second] < ord[i-1][comp[i][b].second];
            else return ord[i-1][comp[i][a].first] < ord[i-1][comp[i][b].first];
        });
        for(int j = 0; j < 3; ++j) ord[i][tmp[j]] = j;
    }
    for(int i = 0; i < 3; ++i) for(int j = 0; j < 3; ++j) lol[0][i][j] = (i == j);
    for(int i = 1; i <= N; ++i){
        for(int j = 0; j < 3; ++j){
            for(int k = 0; k < 3; ++k){
                lol[i][j][k] = lol[i-1][j][k] + lol[i-1][(j+1)%3][k];
            }
        }
    }
    for(int tc = 1; tc <= TC; ++tc){
        int n, p, r, s;
        scanf("%d %d %d %d", &n, &r, &p, &s);
        cm = 0;
        int t = -1;
        for(int i = 0; i < 3; ++i){
            if(p == lol[n][i][0] && r == lol[n][i][1] && s == lol[n][i][2]) t = i;
        }
        if(t == -1) printf("Case #%d: IMPOSSIBLE\n", tc);
        else{
            recur(n, t);
            printf("Case #%d: %s\n", tc, buf);
        }
    }
}
        
