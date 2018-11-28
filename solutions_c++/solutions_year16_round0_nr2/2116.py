#include <iostream>
#include <string>
using namespace std;

int main() {
    int t; cin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        string str; cin >> str;
        str += "+";
        int answer = 0;
        for(int i = 0; i < str.length() - 1; ++i)
            if(str[i] != str[i + 1]) answer++;
        cout << "Case #" << tt << ": " << answer << "\n";
    }
}
