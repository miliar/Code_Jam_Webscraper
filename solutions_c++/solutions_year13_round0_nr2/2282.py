#include <ctime>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <cstdio>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <string.h>
using namespace std;


int main() {
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    
    int T;
    int N, M;
    
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> M;
        vector< vector<int> > a ( N, vector<int> (M) );
        
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                cin >> a[i][j];
            }
        }
        
        bool ok = true;
        for (int i = 0; i < N; ++i) {
            if (!ok) break;
            for (int j = 0; j < M; ++j) {
                if (!ok) break;
                int num = a[i][j];
                bool okRow = true, okCol = true;
                for (int col = 0; col < M; ++col)
                    if (a[i][col] > num) okRow = false;
                for (int row = 0; row < N; ++row)
                    if (a[row][j] > num) okCol = false;
                ok = okRow || okCol;
                
            }
        }
        
        printf("Case #%d: %s\n", t, ok ? "YES" : "NO");
    }
    return 0;
}