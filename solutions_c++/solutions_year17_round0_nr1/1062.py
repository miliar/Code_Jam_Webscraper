#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

char flip(char c) {
    if (c == '+') return '-';
    else return '+';
}

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 0; t1 < t; ++t1) {
        cout << "Case #" << t1 + 1 << ": ";
        string s;
        int k;
        cin >> s >> k;
        int count = 0;
        for (int i = 0; i < s.size() - k + 1; ++i) {
            if (s[i] == '+')
                continue;
            ++count;
            for (int j = 0; j < k; ++j)
                s[i + j] = flip(s[i + j]);
        }
        bool flag = true;
        for (int i = 0; i < s.size(); ++i)
            if (s[i] == '-')
                flag = false;
        if (flag)
            cout << count;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }
}
