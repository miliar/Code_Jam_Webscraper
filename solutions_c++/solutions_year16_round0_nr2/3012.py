#include <iostream>

using namespace std;

int main() {
    
    int casen;
    cin >> casen;
    for (int t = 1; t <= casen; t++) {
        string s;
        cin >> s;
        s.erase(std::unique(s.begin(), s.end()), s.end());
        cout << "Case #" << t << ": " << s.length() - (s[s.length()-1] == '+') << endl;
    }

}
