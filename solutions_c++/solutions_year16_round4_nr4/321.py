#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
typedef pair<int,int> pi;
int TC;
int N;
bool id[5][5];
char grid[5][5];
bool safe(int mach, int ppl){
    for(int i = 0; i < N; ++i){
        if(ppl & (1 << i)) continue;
        bool good = true, found = false;
        for(int j = 0; j < N; ++j){
            if(mach & (1 << j)) continue;
            if(!id[i][j]) continue;
            if(!safe(mach | (1<<j), ppl | (1<<i))) good = false;
            else found = true;
        }
        if(!good || !found) return false;
    }
    return true;
}
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%d", &N);
        for(int i = 0; i < N; ++i){
            scanf("%s", grid[i]);
        }
        int ans = 100000000;
        for(int bs = 0; bs < (1 << (N*N)); ++bs){
            bool vio = false;
            int cost = 0;
            for(int i = 0; i < N; ++i){
                for(int j = 0; j < N; ++j){
                    if((1 << (i*N+j)) & bs) id[i][j] = true;
                    else id[i][j] = false;
                    if(id[i][j] == false && grid[i][j] == '1') vio = true;
                    if(id[i][j] == true && grid[i][j] == '0') ++cost;
                }
            }
            if(vio) continue;
            if(safe(0, 0)) ans = min(ans, cost);
        }
        printf("Case #%d: %d\n", tc, ans);
    }
}
