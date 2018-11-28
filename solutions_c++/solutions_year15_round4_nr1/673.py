#include <cstdio>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <complex>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector<vector<int> > graph;
const int INF = 1000000000;
const ll MOD = 1000000009;
#define FILEIN "A.in"
#define FILEOUT "A.out"



int main(){
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_){
    	
        
        int R, C;
        cin >> R >> C;
        char c[R][C];
        int dirs[R][C];
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                cin >> c[i][j];
                
            }
        }
        int cnt = 0;
        bool f = true;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (c[i][j] == '.') {
                    continue;
                }

                int up = 0;
                int down = 0;
                int left = 0;
                int right = 0;
                for (int k = 1; i + k < R; ++k) {
                    if (c[i+k][j] != '.') {
                        down = 1;
                    }
                }
                for (int k = -1; i + k >= 0; --k) {
                    if (c[i+k][j] != '.') {
                        up = 1;
                    }
                }
                for (int k = 1; j + k < C; ++k) {
                    if (c[i][j + k] != '.') {
                        right = 1;
                    }
                }
                for (int k = -1; j + k >= 0; --k) {
                    if (c[i][j + k] != '.') {
                        left = 1;
                    }
                }
                // cout << i << " " << j << " " << up << " " << down << " " << left << " " << right << endl;
                if (c[i][j] == '^' && up == 1) continue;
                if (c[i][j] == '>' && right == 1) continue;
                if (c[i][j] == 'v' && down == 1) continue;
                if (c[i][j] == '<' && left == 1) continue;
                if (right + left + down + up == 0) {
                    f = false;
                }
                cnt += 1;
            }
        }

        cout << "Case #" << _ << ": ";
        //Output answer 
        if (f) {
            cout << cnt;
        } else {
            cout << "IMPOSSIBLE";
        }
        
        cout << "\n";
    }
    return 0;
}