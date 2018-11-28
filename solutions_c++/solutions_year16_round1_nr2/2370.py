#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cassert>


using namespace std;

typedef long long LL;

bool search(int n, int missing_y, int y, int x, int ref, vector<vector<int> >& lines, vector<int>& row_ref, vector<int>& col_ref, vector<int>& ans){
    // check new x
    if(x > 0){
        vector<int>& col = lines[col_ref[x-1]];
        for(int iy = 0; iy < y; ++iy){
            if(iy == missing_y) continue;
            if(col[iy] != lines[row_ref[iy]][x-1]) return false;
        }
    }
    // check new y
    if(y > 0 && y-1 != missing_y){
        vector<int>& row = lines[row_ref[y-1]];
        for(int ix = 0; ix < x; ++ix){
            if(row[ix] != lines[col_ref[ix]][y-1]) return false;
        }
    }

    // complete
    if(y >= n && x >= n){
        ans.resize(n);
        for(int ix = 0; ix < n; ++ix){
            ans[ix] = lines[col_ref[ix]][missing_y];
        }
        return true;
    }

    // next
    assert(ref >= 0);
    assert(ref < n*2-1 || (ref == n*2-1 && y == missing_y));
    if(y < n){
        row_ref[y] = ref;
        if(y == missing_y){
            if(search(n, missing_y, y+1, x, ref, lines, row_ref, col_ref, ans)) return true;
        }else{
            if(search(n, missing_y, y+1, x, ref+1, lines, row_ref, col_ref, ans)) return true;
        }
    }
    if(x < n){
        col_ref[x] = ref;
        if(search(n, missing_y, y, x+1, ref+1, lines, row_ref, col_ref, ans)) return true;
    }
    return false;
}

vector<int> solve(int n, vector<vector<int> >& lines){
    vector<int> res;
    sort(lines.begin(), lines.end());
    vector<int> row_ref(n);
    vector<int> col_ref(n);
    for(int missing_y = 0; missing_y < n; ++missing_y){
        if(search(n, missing_y, 0, 0, 0, lines, row_ref, col_ref, res)) break;
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        int n;
        cin >> n;
        vector<vector<int> > lines(n*2-1, vector<int>(n));
        for(int y = 0; y < n*2-1; ++y){
            for(int x = 0; x < n; ++x){
                cin >> lines[y][x];
            }
        }
        vector<int> res = solve(n, lines);
        cout << "Case #" << t << ":";
        for(int i = 0; i < n; ++i){
            cout << " " << res[i];
        }
        cout << endl;
    }
    return 0;
}

