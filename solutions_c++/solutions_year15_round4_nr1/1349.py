#include <cstdio>
#include <cstring>

int const dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

char a[111][111];
int r, c;

bool checkout(int x, int y, int dir){
    while(true){
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if(nx < 0 || ny < 0 || nx >= r || ny >= c){
            return true;
        }
        if(a[nx][ny] != '.'){
            return false;
        }
        x = nx;
        y = ny;
    }
}

int proc(){
    int ans = 0;
    for(int i = 0; i < r; ++i){
        for(int j = 0; j < c; ++j){
            int dir;
            switch(a[i][j]){
                case '^': dir = 0; break;
                case '>': dir = 1; break;
                case 'v': dir = 2; break;
                case '<': dir = 3; break;
                default: dir = -1;
            }
            if(dir != -1 && checkout(i, j, dir)){
                ++ans;
                int k;
                for(k = 0; k < 4; ++k){
                    if(dir == k) continue;
                    if(!checkout(i, j, k)){
                        break;
                    }
                }
                if(k == 4) return -1;
            }
        }
    }
    return ans;
}

int main(){
    int t;
    scanf("%d", &t);
    for(int ti = 1; ti <= t; ++ti){
        scanf("%d%d", &r, &c);

        memset(a, 0, sizeof(a));
        for(int i = 0; i < r; ++i){
            scanf("%s", a[i]);
        }

        int ans = proc();
        if(ans == -1){
            printf("Case #%d: IMPOSSIBLE\n", ti);
        }else{
            printf("Case #%d: %d\n", ti, ans);
        }
    }
    return 0;
}
