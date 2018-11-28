#include <algorithm>
#include <bitset>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int mybr(int b, int wh) {
    return (wh / b)*b + b - 1;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        bool ans = false;
        int X, R, C;
        cin >> X >> R >> C;
        if(R > C) swap(R, C);
        if(X == 2) {
            if((R*C)&1) {
                ans = true;
            }
        } else if(X == 3) {
            if(R < 3 && C < 3) {
                ans = true;
            }
            if(R == 1) {
                ans = true;
            }
            if(R == 2) {
                if(C == 4) {
                    ans = true;
                }
            }
            if(R == 4) {
                ans = true;
            }
            if((R*C)%3) {
                ans = true;
            }
        } else if (X == 4) {
            if(R == 1) {
                ans = true;
            }
            if(R == 2) {
                ans = true;
            }
            if((R*C)%4) {
                ans = true;
            }
        }
        cout << "Case #" << t << ": " << (ans ? "RICHARD" : "GABRIEL") << "\n";
    }
}
