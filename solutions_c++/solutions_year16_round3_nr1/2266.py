#include <iostream>

using namespace std;

int main() {
    int k;
    cin >> k;
    for (int i = 1; i <= k; ++i) {
        cout << "Case #" << i << ":";
        int n;
        cin >> n;

        int data[n];
        int sum = 0;
        for (int j = 0; j < n; ++j) {
            cin >> data[j];
            sum += data[j];
        }
        while(sum > 0) {
            cout << " ";
            if(sum == 2) {
                for (int j = 0; j < n; ++j) {
                    if(data[j] > 0) cout << (char)(j+'A');
                }
                sum = 0;
            } else if(sum == 3) {
                bool single = false;
                for (int j = 0; j < n; ++j) {
                    if(data[j] == 0) continue;
                    if(data[j] == 2 || single) {
                        cout << (char)(j+'A');
                        data[j]--;
                        sum--;
                        break;
                    } else {
                        single = true;
                    }
                }
            } else {
                int max = -1;
                int max_i = -1;
                for (int j = 0; j < n; ++j) {
                    if(data[j] > max) {
                        max = data[j];
                        max_i = j;
                    }
                }
                data[max_i]--;
                sum--;
                cout << (char)(max_i+'A');
                max = -1;
                max_i = -1;
                for (int j = 0; j < n; ++j) {
                    if(data[j] > max) {
                        max = data[j];
                        max_i = j;
                    }
                }
                data[max_i]--;
                sum--;
                cout << (char)(max_i+'A');
            }
        }

        cout << endl;
    }

    return 0;
}