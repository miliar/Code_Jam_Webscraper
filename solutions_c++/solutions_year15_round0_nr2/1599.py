#include <cstdio>
#include <iostream>
#include <algorithm>
#define MAXP 1005

using namespace std;

int pancakes[MAXP], D, T;

int main(){
    cin >> T;
    for (int t = 1; t <= T; t++){
        cin >> D;
        for (int d = 0; d < D; d++){
            cin >> pancakes[d];
        }
        int besttime = 1<<30;
        for (int level = 1; level < 1001; level++){
            int moves = 0;
            for (int d = 0; d < D; d++){
                moves += (pancakes[d]-1)/level;
            }
            besttime = min(moves+level, besttime);
        }
        cout << "Case #" << t << ": " << besttime << "\n"; 
    }
}
