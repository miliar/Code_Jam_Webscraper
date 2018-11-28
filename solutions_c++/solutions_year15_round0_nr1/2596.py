#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ifstream cin("test.in");
    ofstream cout("test.out");
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        string s;
        int n;
        cin >> n >> s;
    
        int clap = s[0] - '0';
        int add = 0;
        for (int i = 1; i <= n; i++) {
            if (i > clap + add) {
                add += (i - (clap + add));
                clap += (s[i] - '0');
            } else {
                clap += (s[i] - '0');
            }
        }
        cout << "Case #" << cs << ": " << add << "\n";
    }
    return 0;
}
