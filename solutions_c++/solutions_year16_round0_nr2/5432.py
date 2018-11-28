#include <iostream>  

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {

    int t, j, cnt;
    char s[100];
    
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    
    for (int i = 1; i <= t; ++i) {
        
        scanf("%s", s);
        
        j = 1;
        cnt = 1;
        while (s[j] != NULL) {
            if (s[j] != s[j-1]) {
                cnt++;
            }
            j++;
        }
        
        if ((cnt == 2) & (s[0] == '-') & (s[1] == '+')) {
            cnt = 1;
        }
        
        if ((cnt >= 2) & (s[j-1] == '+')) {
            cnt--;
        }
        
        if ((cnt == 1) & (s[0] == '+')) {
            cnt = 0;
        }
        
        
        
        cout << "Case #" << i << ": " << cnt << endl;

        
    }
}