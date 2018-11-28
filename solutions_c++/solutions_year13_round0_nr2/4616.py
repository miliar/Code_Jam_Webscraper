#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int get() { int x; scanf("%d",&x); return x; }


vector<vector<int> > get_board() {
    int r,c;
    scanf("%d %d",&r,&c);
    vector<vector<int> > ret(r, vector<int>(c));
    for(int i=0;i<r;i++)for(int j=0;j<c;j++) {
        ret[i][j] = get();
    }
    return ret;
}

vector<vector<int> > rotate_sort_of(vector<vector<int> >& board) {
    int r = board.size();
    int c = board[0].size();
    vector<vector<int> > new_board(c, vector<int>(r));
    for(int i=0;i<r;i++)for(int j=0;j<c;j++) {
        new_board[j][i] = board[i][j];
    }
    return new_board;
}

int main() {
    int n = get();
    for(int ca=0;ca<n;ca++) {
        printf("Case #%d: ",ca+1);
        vector<vector<int> > board = get_board();
        vector<vector<int> > is_fine = vector<vector<int> >(board.size(), vector<int>(board[0].size()));
        for(int aoeu=0;aoeu<2;aoeu++) {
            for(int i=0;i<board.size();i++) {
                int m = *max_element(board[i].begin(),board[i].end());
                for(int j=0;j<board[i].size();j++) {
                    if (board[i][j]==m) is_fine[i][j] = 1;
                }
            }
            board = rotate_sort_of(board);
            is_fine = rotate_sort_of(is_fine);
        }
        int fail = 0;
        for(int i=0;i<is_fine.size();i++) {
            fail += count(is_fine[i].begin(),is_fine[i].end(),0);
        }
        puts(fail?"NO":"YES");
    }
    return 0;
}
