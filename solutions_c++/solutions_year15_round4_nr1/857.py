#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int R, C;

bool check(int r, int c, vector<vector<char>> map, char s){
    if (s=='.') return 1;
    if (s=='^'){
        while(r>0 && map[r-1][c] =='.') r--;
        if (r==0) return 0;
        return 1;
    }
    if (s=='<'){
        while(c>0 && map[r][c-1] =='.') c--;
        if (c==0) return 0;
        return 1;
    }
    if (s=='>'){
        while(c<C-1 && map[r][c+1] =='.') c++;
        if (c==C-1) return 0;
        return 1;
    }
    if (s=='v'){
        while(r<R-1 && map[r+1][c] =='.') r++;
        if (r==R-1) return 0;
        return 1;
    }
}

int main() {
    int T; cin>>T;
    for(int case_id = 1;case_id<=T;case_id++){
        cin>>R; cin>>C;
        vector<vector<char> > map(R, vector<char>(C, '.'));
        for(int r = 0;r<R;r++){
            for(int c=0;c<C;c++){
                char s; cin>>s;
                map[r][c] = s;
            }
        }
        int change = 0;
        
        for(int r=0;r<R && change>=0;r++){
            for(int c=0;c<C && change>=0;c++) {
                if (check(r, c, map, map[r][c])) continue;
                if (check(r, c, map, '^')||
                    check(r, c, map, '<')||
                    check(r, c, map, '>')||
                    check(r, c, map, 'v')) {change++; continue;}
                change = -1;
            }
        }
        if (change<0)
            printf("Case #%d: IMPOSSIBLE\n", case_id);
        else
            printf("Case #%d: %d\n", case_id, change);
    }
}