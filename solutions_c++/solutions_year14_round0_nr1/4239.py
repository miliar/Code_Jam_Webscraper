#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int first, second, card, candidate[17] = {};
        cin >> first;
        for (int j = 1; j <= 4; j++) {
            for (int k = 1; k <= 4; k++) {
                cin >> card;
                if (j == first) {
                    candidate[card] = 1;
                }
            }
        }

        int answer = -1;
        cin >> second;
        for (int j = 1; j <= 4; j++) {
            for (int k = 1; k <= 4; k++) {
                cin >> card;
                if (j == second && candidate[card]) {
                    answer = (answer == -1 ? card : -2);
                }
            }
        }

        cout << "Case #" << i << ": ";
        if (answer == -2) {
            cout << "Bad magician!";
        } else if (answer == -1) {
            cout << "Volunteer cheated!";
        } else {
            cout << answer;
        }

        cout << endl;
    }

    return 0;
}
