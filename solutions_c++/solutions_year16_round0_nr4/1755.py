#include <iostream>
#include <string>
using namespace std;


int main() {
    int tests; cin >> tests;
    for(int test=1; test<=tests; test++) {
        int k, c, s; cin >> k >> c >> s;
        
        cout << "Case #" << test << ":";
        
        for(int i=0; i<s; i++) {
            cout << " " << (i+1);    
        }
        cout << endl;
    }
}
