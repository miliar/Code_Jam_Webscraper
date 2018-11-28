#include <iostream>
#include <string>
using namespace std;

int T;

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int smax;
        string s;
        cin >> smax >> s;

        int sum = 0, c = 0;
        for (int i = 0; i < smax; i++) {
            sum += s[i]-'0';
            if (i+1 > sum) {
                c += i+1-sum;
                sum += i+1-sum;
            }
        }

        cout << "Case #" << t << ": " << c << endl;
    }
}
