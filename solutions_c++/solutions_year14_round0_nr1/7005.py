#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int caseNum = 0; caseNum < t; caseNum++) {
        cout << "Case #" << (caseNum+1) << ": ";
        int ans1, ans2;
        int result = 0;

        vector<int> first;
        vector<int> second;

        cin >> ans1;
        for (int i = 1; i <= 4; i++) {
            if (i == ans1) {
                int num;
                for (int j = 0; j < 4; j++) {
                    cin >> num;
                    first.push_back(num);
                }
            } else {
                int junk;
                for (int j = 0; j < 4; j++) {
                    cin >> junk;
                }
            }
        }

        cin >> ans2;
        for (int i = 1; i <= 4; i++) {
            if (i == ans2) {
                int num;
                for (int j = 0; j < 4; j++) {
                    cin >> num;
                    second.push_back(num);
                }
            } else {
                int junk;
                for (int j = 0; j < 4; j++) {
                    cin >> junk;
                }
            }
        }

        int flag = 0;
        for (int i = 0; i < 4 && flag == 0; i++) {
            for (int j = 0; j < 4 && flag == 0; j++) {
                if (first[i] == second[j]) {
                    if (result == 0) {
                        result = first[i];
                    } else {
                        cout << "Bad magician!" << endl;
                        flag = 1;
                    }
                }
            }
        }

        if (result == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if (flag == 0) {
            cout << result << endl;
        }
        
    }
}