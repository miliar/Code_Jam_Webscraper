#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const* argv[])
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        string last_word;
        cin >> s;
        for (int i = 0; i < s.length(); i++) {
            if (i == 0) {
                last_word.push_back(s[i]);
            } else if (last_word[0] <= s[i]) {
                last_word.insert(last_word.begin(),s[i]);
            } else {
                last_word.push_back(s[i]);
            }
        }
        cout << "Case #" << t << ": " << last_word << endl;
    }
    return 0;
}
