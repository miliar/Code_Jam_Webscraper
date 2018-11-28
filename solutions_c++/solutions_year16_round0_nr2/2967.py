#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream fi("b.in");
    ofstream fo("b.out");
    
    int t;
    fi >> t;
    
    for (int i(0); i<t; i++) {
        string s;
        fi >> s;
        
        int last_idx = s.size()- 1;
        while (last_idx >= 0 && s[last_idx] == '+') {
            last_idx--;
        }
        
        if (last_idx < 0) {
            fo << "Case #" << i + 1 << ": 0" << endl;
        } else {
            int count = 0;
            int j = 0;
            while (j < last_idx) {
                if (s[j] == '+') {
                    if (j == 0) {
                        count++;
                    } else {
                        count += 2;
                    }
                    while (j < last_idx && s[j] == '+') {
                        j++;
                    }
                } else {
                    j++;
                }
            }
            count++;
            fo << "Case #" << i + 1 << ": " << count << endl;
        }
    }
    
    fi.close();
    fo.close();
    return 0;
}