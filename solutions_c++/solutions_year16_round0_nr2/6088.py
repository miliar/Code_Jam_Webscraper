#include <iostream>
#include <string>
#include <vector>

using namespace std;

string flip(string s, int n) {
    int m = (n + 1) / 2;

    for(int i = 0; i < m; i++) {
        int j = n - i - 1;
        char c = s[i];

        s[i] = s[j] == '-' ? '+' : '-';
        s[j] = c == '-' ? '+' : '-';
    }

    return s;
}

int count(string s) {
    int flips = 0, length = s.size();

    for(int i = length - 1; i >= 0; i--) {
        if(s[i] == '-') {
            int j = 0;
            while(j < length && s[j] == '+') {
                j++;
            }

            if(j > 0) {
                s = flip(s, j);
                flips++;
            }

            s = flip(s, i + 1);
            flips++;
        }
    }

    return flips;
}

int main(int argc, char **argv) {
    int t;
    cin >> t;

    vector<string> s(t);
    for(int i = 0; i < t; i++) {
        cin >> s[i];
    }

    for(int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": " << count(s[i]) << endl;
    }

    return 0;
}
