#include <iostream>
#include <string>

using namespace std;

const char OFF = '0';

int main() {
    
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int n;
        string s;
        cin >> n >> s;

        int friends = 0;
        int cur = s[0] - OFF;
        for(int i = 1; i < s.length(); i++) {
            if(cur < i) {
                friends += i - cur;
                cur += i - cur;
            }
            cur += (s[i] - OFF);
        }
        cout << "Case #" << (t + 1) << ": " << friends << endl;
    }
    return 0;
}
