#include <iostream>

using namespace std;

int main() {

    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        int rotations = 0;
        string str;
        cin >> str;
        int m = str.length();
        bool data[m];
        int correct_after = -1;
        for (int j = 0; j < m; ++j) {
            data[j] = (str[j]=='+');
            if(!data[j]) {
                correct_after = j;
            }
        }
        while(correct_after != -1) {
            int k = 0;
            while(k < m && data[k]) {
                data[k] = false;
                k++;
            }
            if(k > 0) {
                rotations++;
            }
            while(k < m && !data[k]) {
                k++;
            }
            for (int j = 0; j <= correct_after / 2; ++j) {
                bool tmp = data[j];
                data[j] = !data[correct_after-j];
                data[correct_after-j] = !tmp;
            }
            rotations++;
            correct_after -= k;
        }

        cout << "Case #" << i << ": " << rotations << endl;
    }

    return 0;
}