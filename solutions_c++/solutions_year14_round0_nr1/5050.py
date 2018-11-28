#include <sstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdint>

#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <set>

#include <string>

#include <stdint.h>
#include <limits>

/*
Input 
 	
Output 
 
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
*/

using namespace std;
typedef pair<int, int> pii;

int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int a1[4][4], a2[4][4];
    int N;
    string row;
    const double gap = 10e-6;
    cin >> N;
    int i = 0;
    while (i++ < N) {
        int r1, r2;
        int ans = 0;
        int ret = 0;
        cin >> r1;
        for (int k = 0; k < 4; k++)
            for (int l = 0; l < 4; l++)
                cin >> a1[k][l];
        cin >> r2;
        for (int k = 0; k < 4; k++)
            for (int l = 0; l < 4; l++)
                cin >> a2[k][l];

        for (int k = 0; k < 4; k++)
            for (int l = 0; l < 4; l++)
                if (a1[r1-1][k] == a2[r2-1][l]) {
                    ans++;
                    ret = a1[r1-1][k];
                }
        if (ans == 1)
            cout << "Case #" <<  i << ": " << ret << endl;
        else if (ans == 0)
            cout << "Case #" <<  i << ": " << "Volunteer cheated!" << endl;
        else
            cout << "Case #" <<  i << ": " << "Bad magician!" << endl;
    }
}
