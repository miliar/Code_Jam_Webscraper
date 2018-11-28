#include<cstdio>

int N, M;
int height[110][110];

bool check(int x, int y){
    bool f = true;
    for(int i = 0; i < N && f; i++){
        if(height[i][y] > height[x][y]) f = false;
    }
    if(f) return true;
    f = true;
    for(int i = 0; i < M; i++){
        if(height[x][i] > height[x][y]) f = false;
    }
    return f;
}

int main(){
    freopen("pbout.txt", "w", stdout);
    int T;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d%d", &N, &M);
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++) scanf("%d", &height[i][j]);
        }
        bool f = true;
        for(int i = 0; i < N && f; i++){
            for(int j = 0; j < M && f; j++){
                if(!check(i,j)) f = false;
            }
        }
        printf("Case #%d: %s\n", ++cnt, f?"YES":"NO");
    }
    return 0;
}
