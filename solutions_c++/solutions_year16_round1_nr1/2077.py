#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int T;
string str, last;

int main() {
    freopen("lastWord.in", "r", stdin);
    freopen("lastWord.out", "w", stdout);
    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> str;
        last = str[0];
        for(int j = 1; j < str.length(); j++) {
            last = (last[0] > str[j]) ? (last + str[j]) : (str[j] + last);
        }
        cout << "Case #" << (i+1) << ": " << last << endl;
    }
}
