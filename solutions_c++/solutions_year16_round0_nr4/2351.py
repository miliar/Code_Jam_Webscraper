#include <iostream>
#include <cassert>

using namespace std;

int main() {
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ":";
        
        int k, c, s;
        cin >> k >> c >> s;
        
        assert(k == s);
        
        for (int i = 1; i <= k; i++) cout << " " << i;
        cout << endl;
    }
    
}