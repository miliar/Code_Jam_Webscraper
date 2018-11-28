#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    //t = 1;
    for (int i = 1; i <= t; i++) {
        int n;
        cin >> n;
       // n = 3;
        int pole[n];
        for (int j = 0; j < n; j++) {
            cin >> pole[j];
        }
       //pole[0] = 2;
       //pole[1] = 3;
       //pole[2] = 1;
        cout << "Case #" << i << ":";


        bool flag = false;
        while (!flag) {

            if (n == 2 && pole[0] == 0 && pole[1] == 0) {
                break;
            }

            if (n == 2 && pole[0] == pole[1]) {
                pole[0]--;
                pole[1]--;
                cout << " AB";
                continue;
            }

            bool flaggy = false;
            int flaggyIndex;
            int flagIndex;
            for (int j = 0; j < n; j++) {
                if (pole[j] == 1 && flaggy == true && flag == false) {
                    flag = true;
                    flagIndex = j;
                } else if (pole[j] == 1 && flaggy == false) {
                    flaggy = true;
                    flaggyIndex = j;
                } else if (pole[j] == 0) {
                    continue;
                } else {
                    flag = false;
                    break;
                }
            }
            if (!flag) {
                int max = pole[0];
                int maxIndex = 0;
                for (int j = 0; j < n; j++) {
                    if (pole[j] > max) {
                        max = pole[j];
                        maxIndex = j;
                    }
                }
                pole[maxIndex]--;
                cout << " " << (char)('A'+maxIndex);
            } else {
                cout << " " << (char)('A'+flaggyIndex) << (char)('A'+ flagIndex);
            }
        }
        cout << endl;
    }
    return 0;
}

