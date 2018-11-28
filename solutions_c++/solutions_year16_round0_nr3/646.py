#include <iostream>
#include <string>
#include <bitset>
using namespace std;

const long N = 32;  // Be sure to change this!

int main() {
    long T, J;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ":" << endl;
        cin >> J >> J;
        for (int i = 0; i < J; i++) {
            string s = bitset<N/2-2>(i).to_string();
            s = "1" + s + "1";
            string ss;
            for (char c : s) ss.push_back(c), ss.push_back(c);
            cout << ss;
            for (int j = 2; j <= 10; j++) cout << " " << j + 1;
            cout << endl;
        }
    }
}
