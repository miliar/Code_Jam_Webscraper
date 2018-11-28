#include <iostream>
//#include <cstdlib>
//#include <string>

using namespace std;

int main() {

    int sum, add, size, numOfRound;
    string s;

    cin >> numOfRound;

    for (int round = 1; round <= numOfRound; ++round) {

        sum = 0; add = 0;
        cin >> size >> s;

        for (int i = 0; i <= size; ++i) {
            int aud = s[i] - '0';
            
            if (aud == 0) { continue; }
            else if (i == 0 || i <= sum) { sum += aud; }
            else if (i > sum) {
                add += i - sum;
                sum += i - sum + aud;
            } else {
                // never reach
            }
        }

        cout << "Case #" << round << ": " << add << endl;
    }

    return 0;
}
