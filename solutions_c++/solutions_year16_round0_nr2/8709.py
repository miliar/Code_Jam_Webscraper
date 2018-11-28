#include <iostream>

using namespace std;

int T;
char S[101];

int main() {
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> S;
        bool happy = S[0] == '+';
        int count = 0;
        for (int i = 1; S[i] != '\0'; i++) {
            bool happyTop = S[i] == '+';
            if (happy ^ happyTop) {
                count++;
                happy = happyTop;
            }
        }
        if (!happy) {
            count++;
        }
        cout << "Case #" << test_case << ": " << count << endl;
    }

    return 0;
}
