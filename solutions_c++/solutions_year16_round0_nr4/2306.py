#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ifstream fi("d.in");
    ofstream fo("d.out");
    
    int t;
    fi >> t;
    
    for (int i(0); i<t; i++) {
        int k, c, s;
        fi >> k >> c >> s;
        
        fo << "Case #" << i + 1 << ":";
        
        if (c == 1) {
            if (s < k) {
                fo << " IMPOSSIBLE" << endl;
            } else {
                for (int j(1); j<=k; j++) {
                    fo << " " << j;
                }
                fo << endl;
            }
            continue;
        }
        
        if (k == 1) {
            fo << " 1" << endl;
            continue;
        }
        
        if (s >= k - 1) {
            for (int j=2; j<=k; j++) {
                fo << " " << j;
            }
            fo << endl;
        }
   }
    
    fi.close();
    fo.close();
    return 0;
}