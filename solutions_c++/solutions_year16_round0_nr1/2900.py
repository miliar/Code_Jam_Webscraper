#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    int t, n;
    
    ifstream fi("A.in");
    ofstream fo("A.out");
    
    fi >> t;
    
    for (int i(0); i<t; i++) {
        fi >> n;
        if (n == 0) {
            fo << "Case #" << i + 1 << ": INSOMNIA" << endl;
        } else {
            int flag = 0;
            long long x = n;
            while (1) {
                long long val = x;
                while (val > 0) {
                    flag |= (1 << (val%10));
                    val /= 10;
                }
                if (flag == 1023) {
                    fo << "Case #" << i + 1 << ": " << x << endl;
                    break;
                }
                x += n;
            }
        }
    }
    
    fi.close();
    fo.close();
    
    return 0;
}