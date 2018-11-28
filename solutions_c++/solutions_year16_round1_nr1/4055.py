#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int T;
    string s;
    cin >> T;
    ofstream fout ("a-large-the-last-word.txt");
    for (int t = 1; t <= T; t++) {
        cin >> s;
        string out = "";
        out += s[0];
        for (int i = 1; i < s.size(); i++) {
            if (s[i] < out[0]) {
                out += s[i];
            } else {
                out = s[i] + out;
            }
        }
        cout << "Case #" << t << ": " << out << endl;
        fout << "Case #" << t << ": " << out << endl;
    }
    fout.close();
}
