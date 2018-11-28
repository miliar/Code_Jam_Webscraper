#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>
#include <string>

using namespace std;

int solve(int R, int C, vector<string>& board){
    int ans = 0;
    for(int y = 0; y < R; y++){
        for(int x = 0; x < C; x++){
            if(board[y][x] == '.') continue;
            int dx = 0, dy = 0;
            if(board[y][x] == '^'){
                dy = -1;
                dx = 0;
            }else if(board[y][x] == '>'){
                dx = 1;
                dy = 0;
            }else if(board[y][x] == '<'){
                dx = -1;
                dy = 0;
            }else if(board[y][x] == 'v'){
                dy = 1;
                dx = 0;
            }
            int tx = x + dx;
            int ty = y + dy;
            bool flag = false;
            while(tx >= 0 && ty >= 0 && ty < R && tx < C){
                if(board[ty][tx] != '.'){
                    flag = true;
                    break;
                }
                tx += dx;
                ty += dy;
            }
            if(flag) continue;
            for(tx = 0; tx < C; tx++){
                if(tx == x) continue;
                if(board[y][tx] != '.') flag = true;
            }
            for(ty = 0; ty < R; ty++){
                if(ty == y) continue;
                if(board[ty][x] != '.') flag = true;
            }
            if(!flag) return -1;
            ans += 1;
        }
    }
    return ans;
}



int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int R, C;
        cin >> R >> C;
        vector<string> board(R);
        for(int i = 0; i < R; i++){
            cin >> board[i];
        }
        int ans = solve(R, C, board);
        if(ans >= 0){
            cout << "Case #" << t <<": " << ans << endl;
        }else{
            cout << "Case #" << t <<": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

