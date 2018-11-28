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

#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
#define dbg(args...) {debug,args; cerr << endl;}

#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define P1(a) (a).first
#define P2(a) (a).second
#define T1(a) (a).first
#define T2(a) (a).second.first
#define T3(a) (a).second.second
#define INF 1e20
#define EPS 1e-8

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<int,pii> tiii;

class debu{
    public:
    template<class someClass>
	debu & operator,(someClass arg){
		cerr << arg << " ";
		return *this;
	}
} debug;


void init(){
    cout << setprecision(8)<< fixed;
}

int test(vector< vector<char> > m, int i, int j, int R, int C) {
    int di = 0, dj = 0;
    switch (m[i][j]) {
        case 'v': di = 1; break;
        case '>': dj = 1; break;
        case '<': dj = -1; break;
        case '^': di = -1; break;
        case '.': return 0;
    }
    int pi = i, pj = j;
    pi+= di;
    pj+= dj;    
    while (pi >= 0 && pi < R && pj>=0 && pj < C) {
        if (m[pi][pj] != '.') return 0;
        pi+= di;
        pj+= dj;    
    }
    for (int r = 0; r < R; r++) {
        if (r==i) continue;
        if (m[r][j] != '.') return 1;
    }
    for (int c = 0; c < C; c++) {
        if (c==j) continue;
        if (m[i][c] != '.') return 1;
    }
    return -1;
}

void solve(int testnr){
    int R, C;
    cin >> R >> C;
    vector<vector<char> > maze;
    maze.resize(R);
    for (int i=0; i < R; i++) {
        maze[i].resize(C);
        for (int j=0; j < C; j++) {
            char c;
            cin >> c;
            maze[i][j] = c;
        }
    }
    int res = 0;
    for (int i=0; i < R; i++) {
        for (int j=0; j < C; j++) {
            int t = test(maze, i, j, R, C);
            //dbg(i,j,R,C,t);
            if (t == -1) {
                cout << "IMPOSSIBLE";
                return;
            }
            res += t;
        }
    }
    cout << res;
    return;
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i << ": ";
        solve(i);
        cout << "\n";
    }
    
    return 0;
}
