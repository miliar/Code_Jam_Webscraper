#include <deque>
#include <iostream>
#include <string>

using namespace std;

string last_word(string word) {
    deque<char> out;
    for (auto c : word) {
        if (out.empty())
            out.push_back(c);
        else if (c >= out[0])
            out.push_front(c);
        else
            out.push_back(c);
    }
    return string(begin(out), end(out));
}


int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string word;
        cin >> word;
        string out = last_word(word);
        cout << "Case #" << (i+1) << ": " << out << endl;
    }
    return 0;
}