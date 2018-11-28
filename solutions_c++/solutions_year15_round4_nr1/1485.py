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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#include <fstream>
//#include <iostream>
using namespace std;

ifstream cin("/users/naginahas/Downloads/GCJ2015round2/A-Large.in");
ofstream cout("/users/naginahas/Documents/Codeforces205/GCJ2015Round2A/ALarge.txt");

char grid[200][200];
map <int, pair <int,int> > mp;


bool fullyisol(int i,int j, int R, int C){//assumes grid[i][j] is an arrow
    int cnt = 0;
    for(int k = 0;k<C;k++){
        if(grid[i][k] == '.') cnt++;
    }
    for(int k=0;k<R;k++){
        if(grid[k][j] == '.') cnt++;
    }
    int n= R+C-1-cnt;
    if(n==1) return true;
    else return false;
    
}
bool pisol(int i,int j, int R, int C,pair<int,int> dir){
    int diri = dir.first;
    int dirj = dir.second;
    int curi = i+diri;
    int curj = j+dirj;
    bool found = false;
    while(curi>=0 && curi < R && curj >=0 && curj<C){
        if(grid[curi][curj]!='.') {
            found = true;
            break;
        }
        curi = curi + diri;
        curj = curj + dirj;
        
    }
    if(found){
        return false;
    }
    else return true;
    
    
}


int main(){
    int T;
    cin >> T;
    pair <int,int> rt = make_pair(0,1);
    pair <int,int> lt = make_pair(0,-1);
    pair <int,int> up = make_pair(-1,0);
    pair <int,int> down = make_pair(1,0);
    mp[int('>')] = rt;
    mp[int('<')] = lt;
    mp[int('^')] = up;
    mp[int('v')] = down;
    
    for(int t=0;t<T;t++){
        int R, C;
        cin >> R >> C;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                char c;
                cin >> c;
                grid[i][j] = c;
            }
        }
        bool feasible = true;
        int cnt=0;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(grid[i][j] == '.') continue;
                if(fullyisol(i,j,R,C)){
                    feasible = false;
                }
                if(pisol(i,j,R,C, mp[int(grid[i][j])])){
                    cnt++;
                }
                
            }
        }
        if(feasible){
            cout << "Case #"<< t+1<< ": " << cnt << endl;
            
        }
        else cout << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
        
    }
    return 0;
}
