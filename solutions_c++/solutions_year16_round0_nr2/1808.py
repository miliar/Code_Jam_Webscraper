#include <iostream>
#include <string>
using namespace std;


int main() {
    int tests; cin >> tests;
    for(int test=1; test<=tests; test++) {
        string s; cin >> s;
        int count = 0; char last = ' ';
        for(int i=0; i<s.size(); i++) {
            if (s[i] != last) {
                count++;
                last = s[i];
            }
        }       
        if (last == '+') count--;
        
        cout << "Case #" << test << ": " << count << endl;
    }
}
