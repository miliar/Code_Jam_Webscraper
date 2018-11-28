#include <iostream>
#include <string>

using namespace std;

void lastWord(string s) {
    string t = "";
    t = t + s.at(0);
    for (int i=1; i<s.length(); i++) {
        if (t.at(0) > s.at(i))
            t = t + s.at(i);
        else
            t = s.at(i) + t;
    }
    cout << t << endl;
}

int main() {
    int n; string s;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> s;
        cout << "Case #" << i+1 << ": "; lastWord(s);
    }
    return 0;
}
