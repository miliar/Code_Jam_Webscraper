#include <iostream>
#include <string>

using namespace std;

int T;

int main() {
    cin >> T;
    for (int i = 1; i <= T; i++) {
        string word;
        cin >> word;
        string res = word.substr(0, 1);
        for (int j = 1; j < word.length(); j++) {
            if (word[j] < res[0]) {
                res += word[j];
            } else {
                res = word[j] + res;
            }
        }
        cout << "Case #" << i << ": " << res << endl;
    }
}
