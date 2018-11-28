#include <iostream>
#include <cstdio>

using namespace std;

int main( void ) {
    int TA; cin >> TA;
    
    for(int t = 1; t <= TA; t++) {
        string s;
        cin >> s;
        
        string ss = "";
        for(int i = 0; i < s.size(); i++) {
            int j = i;
            while( j < s.size() && s[j] == s[i] ) {
                j++;
            }
            
            if( j == s.size() && s[i] == '+' ) break;
            
            ss += s[i];
            i = j - 1;
            
        }
        cout << "Case #" << t << ": " << ss.size() << endl;
    }
}