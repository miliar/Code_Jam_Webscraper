#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
using namespace std;

int main() {
    //    freopen("input.txt", "rt", stdin);
    //    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);

    int T, K, C, S;
    cin >> T;
    
    for (int i = 1; i <= T; i++) {
        
        cin >> K >> C >> S;
        
        cout << "Case #" << i << ": ";
        
//        if (C-1 + S < K) {
//            cout << "IMPOSSIBLE" << endl;
//            continue;
//        }
        
        for (int j = 1; j <= K; j++)
            cout << j << " ";
        cout << endl;
    }

}

