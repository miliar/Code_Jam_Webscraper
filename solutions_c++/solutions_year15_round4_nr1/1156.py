#include <bits/stdc++.h>

using namespace std;


typedef long long LL;

map<char, pair<int,int>> Dirs = {
    {'>', {0,1}},
    {'v', {1,0}},
    {'<', {0,-1}},
    {'^', {-1,0}}
};


struct Case {

    int R, C;
    vector<vector<char>> board;

    bool any_to_dir(int i, int j, int di, int dj){
        if(i < 0 || i >= R || j < 0 || j >= C) return false;
        if(board[i][j] != '.') return true;
        return any_to_dir(i+di, j+dj, di, dj);
    }

    void input(){
        scanf("%d%d", &R, &C);
        board.resize(R);
        for(int i = 0; i < R; i++){
            char data[105];
            scanf("%s", data);
            board[i].resize(C);

            for(int j = 0; j < C; j++){
                board[i][j] = data[j];
            }
        }
    }

    void run(){
        int result = 0;
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                if(board[i][j] == '.') continue;
                int di = Dirs[board[i][j]].first,
                    dj = Dirs[board[i][j]].second;
                if(any_to_dir(i + di, j + dj, di, dj)) continue;

                int cnt = 0;
                for(auto P : Dirs){
                    int ndi = P.second.first,
                        ndj = P.second.second;
                    if(any_to_dir(i + ndi, j + ndj, ndi, ndj)) cnt++;
                }

                if(cnt == 0){ printf("IMPOSSIBLE\n"); return; }
                result++;
            }
        }
        printf("%d\n", result);
    }
};

int main(){
    int numTests;
    scanf("%d", &numTests);

    for(int i = 1; i <= numTests; i++){
        Case C;
        C.input();
        printf("Case #%d: ", i);
        C.run();
    }
}
