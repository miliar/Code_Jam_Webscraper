#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    string j;
    getline(cin, j);
    
    for (int i = 0; i < n; i++) {
        string s;
        getline(cin, s);
        
        int n = ((s[0] == '+') ? 0 : 1);
        int f = 0;
        for (int j = 0; j < s.length() - 1; j++) {
            if (s[j] != s[j + 1]) f++;
        }
        
        if ((f + n) % 2 == 1) {
            f++;
        }
        
        cout << "Case #" << i + 1 << ": " << f << endl;
    }
}