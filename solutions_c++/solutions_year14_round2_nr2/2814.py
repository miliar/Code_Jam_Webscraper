
#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <string>

#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()

using namespace std;

int main (void) {
    int cases;
    int a, b, k, c;
    
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    
    cin >> cases;
    
    for (int t = 1; t <= cases; t++) {
        cout << "Case #" << t << ": ";
        cin >> a >> b >> k;
        c = 0;
        
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if ((i & j) < k) {
                    c++;
                }
            }
        }
        
        cout << c << endl;
    } 
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
