#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define MAX_N 1000

int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    int x, r, c;
    int win = -1;
    int test = 0;
    while (t--) {
        win = -1;
        cin >> x >> r >> c;
        
        if (r < c)
        swap(r, c);
        
        if (x == 1) win = 1;
        else {
            if (x > r && x > c) win = 0;
            else {
                if ((r * c)%x != 0) win = 0;
                else{
                    if (x == 2) {
                        win = 1;
                    }
                    else if (x == 3) {
                        if (r == 3 && c == 1) win = 0;
                        else if (r == 3 && c == 2) win = 1;
                        else if (r == 3 && c == 3) win = 1;
                        else if (r == 4 && c == 3) win = 1;
                    }
                    else if (x == 4) {
                        if (r == 4 && c == 1) win = 0;
                        if (r == 4 && c == 2) win = 0;
                        if (r == 4 && c == 3) win = 1;
                        if (r == 4 && c == 4) win = 1;
                    }
                }
            }
        }
        
        test++;
        cout << "Case #" << test << ": ";
        if (win == 1) cout << "GABRIEL" << endl;
        else cout << "RICHARD" << endl;
    }
    
    return 0;
}


