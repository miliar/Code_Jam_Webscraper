#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

void solve() {
    ll B, M;
    cin >> B >> M;
    
    if(M > (1L << (B - 2))) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        cout << "POSSIBLE" << endl;
        vector<vector<bool> > slide(B, vector<bool>(B, false));
        for(int i = 0; i < B-1; ++i) {
            for(int j = i+1; j < B-1; ++j) {
                slide[i][j] = true;
            }
        }
        
        ll ways = M;
        ll shift = B - 3;
        while(shift >= 0) {
            ll v = (1L << shift);
            if(v <= ways) {
                ways -= v;
                slide[shift+1][B-1] = true;
            }
            shift--;
        }
        if(ways == 1) {
            slide[0][B-1] = true;
            ways--;
        }
        
        if(ways != 0) {
            cout << "LOOOL" << endl;
        }
        
        for(vector<bool>& row : slide) {
            for(bool s : row)
                cout << s;
            cout << endl;
        }
    }
    
}

int main() {
     
    int c = 1;
    int T;
    cin >> T;
    while(T --> 0) {
        cout << "Case #" << c++ << ": ";
        solve();
    }
    
    return 0;
}
