#include <bits/stdc++.h>

using namespace std;

typedef long long llong;

int mvs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int getDir(char c){
    switch(c){
        case '>': return 3;
        case '<': return 2;
        case 'v': return 1;
        case '^': return 0;
    }
    assert(false);
}

struct Grid{
    vector<string>& g;
    int r, c;

    Grid(vector<string>& g_, int r_, int c_) : g(g_), r(r_), c(c_) {};

    bool isInside(int i, int j){
        return i >= 0 and j >= 0 and i < r and j < c;
    }

    bool isNice(int i, int j, int d){
        int ni = i + mvs[d][0];
        int nj = j + mvs[d][1];
        while(isInside(ni, nj)){
            if(g[ni][nj] != '.') return true;
            ni += mvs[d][0];
            nj += mvs[d][1];
        }
        return false;
    }

    int solve(){
        int cost = 0;
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(g[i][j] != '.'){
                    if(not isNice(i, j, getDir(g[i][j]))){
                        bool impossible = true;
                        for(int d = 0; d < 4; d++){
                            if(isNice(i, j, d)){
                                impossible = false;
                                break;
                            }
                        }
                        if(impossible) return -1;
                        cost++;
                    }
                }
            }
        }
        return cost;
    }

};

int main(){
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; tc++){
        int r, c;
        cin >> r >> c;
        vector<string> g(r);
        for(auto& row : g) cin >> row;
        Grid grid(g, r, c);
        int sol = grid.solve();
        cout << "Case #" << tc << ": ";
        if(sol == -1){
            cout << "IMPOSSIBLE\n";
        }else{
            cout << sol << '\n';
        }
    }
}
