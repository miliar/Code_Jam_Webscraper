#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long ll;



int main(){
    int T;
    cin >> T;
    
    for(int t=1;t<=T;t++){
        int R, C;
        cin >> R >> C;
        vector<string> sgrid(R);
        for(int i=0;i<R;i++) cin >> sgrid[i];
        
        vector<int> grow(C, -1);
        vector<vector<int> > grid(R, grow);
        
        int arrows = 0;
        for(int x=0;x<C;x++){
            for(int y=0;y<R;y++){
                if(sgrid[y][x] != '.'){
                    grid[y][x] = arrows;
                    arrows++;
                }
            }
        }
        
        vector<int> next(arrows, -1);
        vector<int> left(arrows, -1);
        vector<int> right(arrows, -1);
        vector<int> up(arrows, -1);
        vector<int> down(arrows, -1);
        
        for(int x=0;x<C;x++){
            for(int y=0;y<R;y++){
                if(grid[y][x]!=-1){
                    for(int yp=y-1;yp>=0;yp--){
                        if(grid[yp][x]!=-1){
                            up[grid[y][x]] = grid[yp][x];
                            break;
                        }
                    }
                    for(int yp=y+1;yp<R;yp++){
                        if(grid[yp][x]!=-1){
                            down[grid[y][x]] = grid[yp][x];
                            break;
                        }
                    }
                    for(int xp=x-1;xp>=0;xp--){
                        if(grid[y][xp]!=-1){
                            left[grid[y][x]] = grid[y][xp];
                            break;
                        }
                    }
                    for(int xp=x+1;xp<C;xp++){
                        if(grid[y][xp]!=-1){
                            right[grid[y][x]] = grid[y][xp];
                            break;
                        }
                    }
                    
                    if(sgrid[y][x]=='^') next[grid[y][x]] = up[grid[y][x]];
                    if(sgrid[y][x]=='v') next[grid[y][x]] = down[grid[y][x]];
                    if(sgrid[y][x]=='>') next[grid[y][x]] = right[grid[y][x]];
                    if(sgrid[y][x]=='<') next[grid[y][x]] = left[grid[y][x]];
                }
            }
        }
        
        bool good = true;
        int ans = 0;
        for(int i=0;i<arrows;i++){
            if(next[i]==-1){
                if(up[i]+down[i]+left[i]+right[i]==-4) good = false;
                else ans++;
            }
        }
        
        if(good){
            cout << "Case #" << t << ": " << ans << endl;
        }else{
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}