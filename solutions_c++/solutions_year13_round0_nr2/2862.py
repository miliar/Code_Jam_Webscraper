#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Piece {
    int x;
    int y;
    int height;
    Piece(int a, int b) : x(a), y(b), height(100) { };
    Piece(int a, int b, int c) : x(a), y(b), height(c) { };
    bool operator< (const Piece &p2) const {
        return this->height < p2.height;
    }
};

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        cout << "Case #" << c << ": ";
        
        int N, M;
        cin >> N >> M;
        vector< vector<int> > lawn(N, vector<int>(M));
        vector< vector<int> > mark(N, vector<int>(M, 100));
        vector<Piece> seq;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> lawn[i][j];
                seq.push_back(Piece(i, j, lawn[i][j]));
            }
        }
        sort(seq.begin(), seq.end());
        
        int flag = 1;
        for (int k = 0; k < (int) seq.size(); k++) {
            int r = seq[k].x, c = seq[k].y, h = seq[k].height;
            //~ cout << h << endl;
            if (h == mark[r][c]) {
                continue;
            } else if (h > mark[r][c]) {
                flag = 0;
                break;
            } else {
                int cutrow = 1, cutcol = 1;
                for (int j = 0; j < M; j++) {
                    if (lawn[r][j] > h) {
                        cutrow = 0;
                        break;
                    }
                }
                for (int i = 0; i < N; i++) {
                    if (lawn[i][c] > h) {
                        cutcol = 0;
                        break;
                    }
                }
                if (cutrow == 1) {
                    for (int j = 0; j < M; j++) {
                        mark[r][j]= min(mark[r][j], h);
                    }
                }
                if (cutcol == 1) {
                    for (int i = 0; i < N; i++) {
                        mark[i][c]= min(mark[i][c], h);
                    }
                }
                if (cutrow == 0 && cutcol == 0) {
                    flag = 0;
                    break;
                }
            }
        }
        if (flag == 1) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    
    return 0;
}
