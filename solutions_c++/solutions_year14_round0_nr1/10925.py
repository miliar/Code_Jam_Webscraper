#include <iostream>

using namespace std;

int main(int argc, char ** argv) {
    int T, testCase = 0, R1, R2;
    int d[4], a[4], e[4];

    cin >> T;

    while (testCase < T) {
        cin >> R1;

        for (int i = 0; i < 4; ) {
            if (++i == R1) {
                cin >> a[0] >> a[1] >> a[2] >> a[3];
            } else {
                cin >> d[0] >> d[1] >> d[2] >> d[3];
            }
        }

        cin >> R2;
        for (int i = 0; i < 4; ) {
            if (++i == R2) {
                cin >> e[0] >> e[1] >> e[2] >> e[3];
            } else {
                cin >> d[0] >> d[1] >> d[2] >> d[3];
            }
        }

        int correct_answer = 0;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (a[i] == e[j]) {
                    if (correct_answer == 0) {
                        correct_answer = a[i];
                    } else {
                        correct_answer = -1;
                        break;
                    }
                }
            }
            if (correct_answer == -1) break;
        }

        cout << "Case #" << ++testCase << ": ";
        switch (correct_answer) {
            case 0:
            cout << "Volunteer cheated!" << endl;
            break;
            case -1:
            cout << "Bad magician!" << endl;
            break;
            default:
            cout << correct_answer << endl;
        }
    }

    return 0;
}
