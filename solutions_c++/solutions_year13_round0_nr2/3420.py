#include <iostream>
#include <fstream>
#include <array>
#include <utility>
#include <vector> 

using namespace std;

#define I(w,x,y) ((y)*(w)+(x))

struct rayresult {
    int res[4];
    bool init[4] = {false};
};

struct lawn {
    vector<int> grid;
    vector<rayresult> rays;
    int w; int h;

    lawn(int wd, int ht)
        : w(wd), h(ht),
        grid(vector<int>(wd*ht, 0)),
        rays(vector<rayresult>(wd*ht, rayresult()))
    { }
    
    int& operator()(int x, int y) { return grid[y*w+x]; }
    rayresult& cache(int x, int y) { return rays[y*w+x]; }
};

enum dir { U, D, L, R };

int castray(lawn& board, int x, int y, int dir) {
    if (x < 0 || x >= board.w || y < 0 || y >= board.h) return -1;
    if (board.cache(x,y).init[dir]) return board.cache(x,y).res[dir];
    board.cache(x,y).init[dir] = true;
    switch (dir) {
    case D: board.cache(x,y).res[dir] = castray(board, x, y+1, dir); break;
    case U: board.cache(x,y).res[dir] = castray(board, x, y-1, dir); break;
    case L: board.cache(x,y).res[dir] = castray(board, x-1, y, dir); break;
    case R: board.cache(x,y).res[dir] = castray(board, x+1, y, dir); break;
    }
    board.cache(x,y).res[dir] = max(board(x,y), board.cache(x,y).res[dir]);
    return board.cache(x,y).res[dir];
}

int main(int argc, char **argv) {
    if (argc < 2) {
        cout << "Expected argument\n";
        exit(1);
    }

    ifstream file(argv[1]);
    int ncases;
    file >> ncases;
    for (int i = 0; i < ncases; i++) {
        cout << "Case #" << i + 1 << ": ";
        
        int w, h;
        file >> w >> h;
        lawn board(w, h);
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                int p;
                file >> p;
                board(i, j) = p;
            }
        }

        for (int i = 0; i < board.w; i++) {
            for (int j = 0; j < board.h; j++) {
                bool ok = false;
                ok |= (castray(board, i, j, U) <= board(i,j) && castray(board, i, j, D) <= board(i,j));
                ok |= (castray(board, i, j, L) <= board(i,j) && castray(board, i, j, R) <= board(i,j));

                if (!ok) {
                    cout << "NO";
                    goto no;
                }
            }
        }

        cout << "YES";
no:
        cout << "\n";
    }
}
