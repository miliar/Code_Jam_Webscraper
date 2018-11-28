#include <iostream>

using namespace std;

int main() {
    
    int t, j, cnt;
    char s[1000];
    string res;
    
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    
    for (int i = 1; i <= t; ++i) {
        
        scanf("%s", s);

        res = s[0];
        
        int j = 1;

        while (s[j] != NULL) {
            if (s[j] >= res.front())
                res = s[j] + res;
            else
                res = res + s[j];
            j++;
        }
        
        
        
        
        cout << "Case #" << i << ": " << res << endl;
        
        
    }
}