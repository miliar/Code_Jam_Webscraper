#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        int s;
        cin >> s;
        string shyness;
        cin >> shyness;
        int stoodUp = 0;
        int res = 0;
        for (int i = 0; i < s + 1; i++) {
            int cnt = shyness[i] - '0';
            if (cnt != 0 && stoodUp < i) {
                res += i - stoodUp;
                stoodUp = i;
            }
            stoodUp += cnt;

        }
        cout << "Case #" << tt << ": " << res << "\n";
    }
    return 0;
}
