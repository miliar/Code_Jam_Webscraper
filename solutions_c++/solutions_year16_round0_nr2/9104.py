#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; ++i) {
        string s;
        int count = 0;
        bool flip = false;
        cin >> s;
        
        if (s[0] == '-') {
            flip = true;
            count = 1;
        }

        for (int j = 1; j < s.size(); j++) {
            if (s[j] == '+' && flip) {
                flip = false;
            } else if (s[j] == '-' && !flip) {
                count += 2;
                flip = true;
            } 
        }
        cout << "Case #" << i + 1 << ": " << count << endl;
    }
}
