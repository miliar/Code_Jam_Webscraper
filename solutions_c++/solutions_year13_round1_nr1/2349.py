
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <sstream>
#include <utility>
#include <string>
#include <vector>

#define debug if(0)

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main (void) {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    
    int cases;
    ull count, r, t;
    ull tinta, area;
    ull pi = (ull) (M_PI * 1000000000);
    
    cin >> cases;
    
    for (int c = 1; c <= cases; c++) {
        count = 0;
        cin >> r >> t;
        r++;
        
        tinta = pi * t;
        area = 0;
                
        while (true) {
            area += (pi * r * r) - (pi * (r-1) * (r-1));
            if (tinta < area) break;
            
            r += 2;
            count++;
        }
        
        cout << "Case #" << c << ": " << count << endl;
    }
    
    return 0;
}
