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

#define in(x,y) (2*((x)*H + (y)))
#define out(x,y) (2*((x)*H + (y)) + 1)
#define IN (2*(W*H))
#define OUT (2*(W*H)+1)

int W, H, B, N;
vector<set<int> > adlist;
vector<int> visited;

int dfs(int pos){
    if (pos == OUT) return 1;
    visited[pos] = 1;
    for(set<int>::iterator it = adlist[pos].begin(); it != adlist[pos].end(); it++){
        if (!visited[*it]) {
            if (dfs(*it)){
                adlist[*it].insert(pos);
                adlist[pos].erase(*it);
                return 1;
            }
        }
    }
    return 0;
}

int solve(int testnr){
    cin >> W >> H >> B;
    vector< vector<int> > blocked(W);
    rep(i,W) blocked[i].resize(H, 0);
    rep(i,B) {
        int x0, x1, y0, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        rep(dx, x1 + 1 - x0) rep(dy, y1 + 1 - y0) blocked[x0+dx][y0+dy] = 1;
    }
    //rep(i,W) rep(j,W) dbg(blocked[i][j]);
    
    if (B==0) return W;
    
    //Graph:
    N = 2*(W * H) + 2;
    adlist.clear();
    adlist.resize(N);
    rep(x,W) rep(y,H){
        if (!blocked[x][y]) {
            for(int Dx = -1; Dx <=1; Dx+=2)
                for(int Dy = -1; Dy <=1; Dy+=2){
                int dx = (Dx+Dy)/2, dy = (Dx-Dy)/2;
                if (x+dx >= 0 && x+dx < W && y+dy >= 0 && y+dy <=H && !blocked[x+dx][y+dy]) {
                    adlist[out(x,y)].insert(in(x+dx, y+dy));
                }
            }
            adlist[in(x,y)].insert(out(x,y));
            if (y==0) {
                adlist[IN].insert(in(x,y));
            }
            if (y==H-1) {
                adlist[out(x,y)].insert(OUT);
            }
        }
    }
    
    //Compute Flow:
    
    rep(flow,W){
        visited.clear();
        visited.resize(N, 0);
        if (!dfs(IN)) return flow;
    }
    
    return W;
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i << ": " << solve(i) << "\n";
    }
    
    return 0;
}
