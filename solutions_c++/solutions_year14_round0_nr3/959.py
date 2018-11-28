#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <sstream>
using namespace std;

class MapGenerator {
private:
    vector<vector<bool>> isMine;
    int R, C, M;
    
    bool SolveRC(int r, int c, int m){
        if (m == 0) return true;
        if (m >= min(r, c) || m < min(r,c) - 1) {
            if (r < c) {
                for (int i = r-1; i >= 0; --i) {
                    if (m == 0) return true;
                    isMine[i][c-1] = true;
                    m--;
                }
                return SolveRC(r, c-1, m);
            } else {
                for (int i = c-1; i >= 0; --i) {
                    if (m == 0) return true;
                    isMine[r-1][i] = true;
                    m--;
                }
                return SolveRC(r-1, c, m);
            }
        } else {
            if (min(r, c) == 2) {
                return false;
            } else {
                // if min(r, c) > 2
                if (r < c) {
                    for (int i = r-1; i > 1; --i) {
                        if (m == 0) return true;
                        isMine[i][c-1] = true;
                        m--;
                    }
                    return SolveRC(r, c-1, m);
                } else {
                    for (int i = c-1; i > 1; --i) {
                        if (m == 0) return true;
                        isMine[r-1][i] = true;
                        m--;
                    }
                    return SolveRC(r-1, c, m);
                }
                return true;
            }
        }
    }
    
public:
    MapGenerator(int R, int C, int M) {
        this->R = R;
        this->C = C;
        this->M = M;
        
        for (int i = 0; i < R; ++i) {
            vector<bool> row;
            for (int j = 0; j < C; ++j) {
                row.push_back(false);
            }
            isMine.push_back(row);
        }
    }
    
    
    
    string GenerateOnlyOne() {
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                isMine[i][j] = true;
            }
        }
        return GenerateMap(0, 0);
    }
    
    string GenerateOneColSolution() {
        int mine_cnt = 0;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (mine_cnt++ < M) {
                    isMine[i][j] = true;
                } else {
                    break;
                }
            }
        }
        
        return GenerateMap(R-1, C-1);
    }
    
    string GenerateMap(int ci, int cj){
        ostringstream oss;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (i == ci && j == cj) {
                    oss<<'c';
                } else {
                    if (isMine[i][j]) {
                        oss<<'*';
                    } else {
                        oss<<'.';
                    }
                }
            }
            oss<<endl;
        }
        return oss.str();
    }
    
    string Solve(){
        if (R * C - M == 1 ) {
            //always has solution
            return GenerateOnlyOne();
        }
        if (min(R, C) == 1 && R * C > M) {
            return GenerateOneColSolution();
        } else {
            if ( R * C - M < 4 ){
                return "Impossible\n";
            }
        }
        if (SolveRC(R, C, M)) {
            return GenerateMap(0, 0);
        } else {
            return "Impossible\n";
        }
    }
};


int main(int argc, const char * argv[])
{
    int T, R, C, M;
    int cnt = 1;
    cin>>T;

    while(T-- > 0){
        cin>>R>>C>>M;
        printf("Case #%d:\n", cnt++);
        MapGenerator mg(R, C, M);
        cout<<mg.Solve();
    }
}