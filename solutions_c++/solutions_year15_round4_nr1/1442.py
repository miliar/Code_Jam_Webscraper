#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

struct Node{
    int y,x;
    bool out;
};

const int DY[] = {1,0,-1,0};
const int DX[] = {0,1,0,-1};
const char DM[] = {'v','>', '^', '<'};
int R,C;

bool valid(int y,int x){
    return y>=0 && x>=0 && y<R && x<C;
}

vector<int> link;
vector<int> used;
pair<bool,int> rec(int v, int d){
    if(used[v]){
        return make_pair(true,d);
    }
    used[v] = 1;
    if(link[v]==-1)return make_pair(false,d);
    return rec(link[v],d+1);
}

int solve(vector<string> field){
    link.assign(R*C, -1);
    REP(y,R){
        REP(x,C){
            if(field[y][x]=='.')continue;
            int dir = 0;
            REP(i,4)if(field[y][x]==DM[i]){
                dir = i;
                break;
            }
            int ny = y + DY[dir];
            int nx = x + DX[dir];
            while(valid(ny,nx) && field[ny][nx]=='.'){
                ny += DY[dir];
                nx += DX[dir];
            }
            if(!valid(ny,nx))continue;
            link[y*C+x] = ny*C+nx;
        }
    }

    int res = 0;
    used.assign(R*C, 0);
    REP(y,R){
        REP(x,C){
            if(field[y][x]=='.')continue;
            if(used[y*C+x])continue;
            pair<bool,int> judge = rec(y*C+x,0);
            //cerr << y << "," << x << ":" << judge.first << " " << judge.second  << endl;
            if(judge.first)continue;
            if(judge.second==0){
                bool ok = false;
                REP(i,4){
                    int ny = y + DY[i];
                    int nx = x + DX[i];
                    while(valid(ny,nx) && field[ny][nx]=='.'){
                        ny += DY[i];
                        nx += DX[i];
                    }
                    if(!valid(ny,nx))continue;
                    ok = true;
                }
                if(!ok)return -1;
                res++;
            }else{
                res++;
            }
        }
    }

    return res;
}

int main(){
    int T;
    cin >> T;
    REP(testCase,T){
        cin >> R >> C;
        vector<string> field(R);
        REP(i,R){
            cin >> field[i];
        }

        int res = solve(field);
        cout << "Case #" << testCase+1 << ": ";
        if(res==-1)cout << "IMPOSSIBLE";
        else cout << res;
        cout << endl;
    }
    return 0;
}
