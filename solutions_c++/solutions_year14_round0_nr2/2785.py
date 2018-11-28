#include <cstdlib>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    double c, f, x;
    
    cin >> T;
    
    for(int k = 1; k <= T; k++){
        
        double sum = 0.0, last = 100000.0, cur = 0, r = 2.0;
        
        cin >> c >> f >> x;
        
        cur = x / r;
        
        while(cur < last){
            last = cur;
            sum += c / r;
            r += f;
            cur = x / r + sum;
        }
        
        
        cout << "Case #" << k << ": ";
        printf("%.7f", last);
        cout << endl;
    }
    
    return 0;
}

