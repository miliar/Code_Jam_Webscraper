#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int k = 1; k <= t; k++) {
        int friendsRequired = 0;
        int currentClaps = 0;
        int Smax = 0;
        string str;

        cin >> Smax;
        cin >> str;
        for (int i = 0; i < Smax + 1; i++) {
            if (i == 0) {
                currentClaps += str[i] - '0';
            }
            else {
                while (currentClaps < i) {
                    friendsRequired++;
                    currentClaps++;
                }
                currentClaps += str[i] - '0';
            }
        }
        cout << "Case #" << k << ": " << friendsRequired << endl;
    }
}
