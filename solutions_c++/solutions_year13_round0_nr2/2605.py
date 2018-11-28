#include <cstdio>
#include <algorithm>

using namespace std;

int grass[104][104];

bool possible(int r, int c){
    if(r <= 1 || c <= 1){
        return true;
    }
    int low = 101;
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            low = min(grass[i][j], low);
        }
    }
    int rr = -1;
    for(int i = 0; i < r; i++){
        bool line = true;
        for(int j = 0; j < c; j++){
            if(grass[i][j] != low){
                line = false;
                break;
            }
        }
        if(line){
            rr = i;
            break;
        }
    }
    if(rr != -1){
        for(int i = 0; i < c; i++){
            grass[rr][i] = grass[r - 1][i];
        }
        return possible(r - 1, c);
    }
    int cc = -1;
    for(int i = 0; i < c; i++){
        bool line = true;
        for(int j = 0; j < r; j++){
            if(grass[j][i] != low){
                line = false;
                break;
            }
        }
        if(line){
            cc = i;
            break;
        }
    }
    if(cc != -1){
        for(int i = 0; i < r; i++){
            grass[i][cc] = grass[i][c - 1];
        }
        return possible(r, c - 1);
    }
    return false;
}

int main(){
    int t;
    scanf("%d\n", &t);
    int ca = 1;
    while(t--){
        int m, n;
        scanf("%d %d\n", &m, &n);
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                scanf("%d", &grass[i][j]);
            }
        }
        printf("Case #%d: ", ca++);
        if(possible(m, n)){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}