// Dark Side of Elephant
// Askar

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <cstring>
#include <algorithm>
#include <utility>
#include <tuple>
#include <complex>
#include <cmath>

using namespace std;

#define FOR(i, N) for(auto i=(N)-(N); i<(N); ++i)
#define FOR1(i, N) for(auto i=(N)-(N)+1; i<=(N); ++i)
#define FOREACH(it, a) for(auto it=(a).begin(); it!=(a).end(); ++it)
#define MAXIM(a,b) a=max(a, static_cast<__typeof__(a)>(b))
#define MINIM(a,b) a=min(a, static_cast<__typeof__(a)>(b))
#define beginend(a) (a).begin(), (a).end()
#define pf printf
#define sf scanf
#define mp make_pair
#define mt make_tuple
#define pass
#define sqr(x) (x)*(x)
typedef long long ll;
typedef pair<long long, long long> pll;
typedef pair<int, int> pii;
const long long INF = 1e9;
const double EPS = 1e-9;

#define dbg if(false)
#ifdef EBUG
    #undef dbg
    #define dbg if(true)
#endif

#define epf(...) fprintf(stderr, __VA_ARGS__)
#define dpf(...) dbg epf(__VA_ARGS__)
#define db(x) dbg cerr << #x << ":\t" << (x) << endl 
#define assert(x, ...) if(!(x)){                                \
epf("L: %i, F: %s: (%s) failed!\n", __LINE__, __FUNCTION__, #x);\
error_exit(__VA_ARGS__);                                        \
}
const int WA = 0;
const int EXC = 1;
const int TLE = 2;
void error_exit(const int exit_type=WA){
    switch(exit_type){
        case WA: epf("\nWe want WA!\n"); exit(0); break; 
        case EXC: exit(47); break;
        case TLE: while(true); break;
    }
}

// DO NOT CHANGE!!
const int EMPTY = 0;
const int START = 1;
const int MINE = 2;
const int REVEALED = 3;
const int WALL = 4;

void dfs_minesweeper(vector<vector<int> > &a, const int x, const int y){
    if(a[x][y] < 2){ // EMPTY or START
        a[x][y] = REVEALED;
        
        int mines = 0;

        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++)if(i != 0 || j != 0){
                if(a[x+i][y+j] == MINE) ++mines;
            }
        }
        
        if(mines == 0){
            for(int i = -1; i <= 1; i++){
                for(int j = -1; j <= 1; j++)if(i != 0 || j != 0){
                    dfs_minesweeper(a, x+i, y+j);
                }
            }
        }

    }
}

bool all_revealed(const vector<vector<int> > &a){
    bool res = true;
    FOREACH(it, a) FOREACH(itt, *it) if(*itt < 2){ res = false; break;} 
    return res;
}

int main(){
    int T;
    sf(" %i", &T);

    for(int t = 1; t <= T; t++){
        int R, C, M;
        sf(" %i %i %i", &R, &C, &M);


        // ! only small instances
        assert(R*C <= 28);
        
        vector<int> grid(R*C, EMPTY);
        for(int i = R*C - M ; i < R*C; i++){
            grid[i] = MINE;
        }
        grid[R*C-M-1] = START;
        dbg{
            FOREACH(it, grid) cerr << *it << " "; cerr << endl;
        }
        
        bool has_solution = false;
        
        vector<vector<int> > matrix(R+2, vector<int> (C+2, WALL));
        pii start;
        do{
            for(int i = 0; i < R; i++){
                for(int j = 0; j < C; j++){
                    matrix[i+1][j+1] = grid[C*i + j];
                    if(grid[C*i + j] == START){
                        start = mp(i+1, j+1);
                    }
                }
            }   
            
            if(0) dbg{
                for(int i = 0; i < R+2; i++){
                    for(int j = 0; j < C+2; j++){
                        cerr << matrix[i][j] << " ";
                    }
                    cerr << endl;
                }
                cerr << "---------------------\n";
            }
            
            dfs_minesweeper(matrix, start.first, start.second);
            if(all_revealed(matrix)){
                // weeeee
                has_solution = true;
                pf("Case #%i:\n", t);
                for(int i = 1; i <= R; i++){
                    for(int j = 1; j <= C; j++){
                        if(mp(i,j) == start) pf("c");
                        else if(matrix[i][j] == REVEALED) pf(".");
                        else if(matrix[i][j] == MINE) pf("*");
                    }
                    pf("\n");
                }
            }
            
        } while(!has_solution && next_permutation(beginend(grid)));
        if(!has_solution){
            pf("Case #%i:\nImpossible\n", t);
        }
    }
}
