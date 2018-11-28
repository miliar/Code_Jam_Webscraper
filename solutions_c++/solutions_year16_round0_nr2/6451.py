#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int main() {
    
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        cout<<"Case #"<<i+1<<": ";
        string s; cin>>s;
        
        char c = '-';
        size_t pos = s.find_last_of(c);
        if ( pos != string::npos) {
            int count = 1;
            int cur_pos = (int) pos;
            while (cur_pos >= 0 ) {
                if(s[cur_pos] == c) {
                    cur_pos--;
                } else {
                    count++;
                    if(c == '-') c = '+';
                    else c = '-';
                }
            }
            cout<<count<<"\n";

        } else {
            cout<<"0\n";
        }
    }
}