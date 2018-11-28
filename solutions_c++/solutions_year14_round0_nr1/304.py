#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        int cards[16] = {};
        for (int i = 0; i < 2; ++i) {
            int row = 0;
            cin >> row;
            for (int j = 0; j < 16; ++j) {
                int cur = 0;
                cin >> cur;
                if (j < row * 4 && j >= (row-1) * 4)
                    cards[cur-1]++;
            }
        }
        int result = 0;
        int found = 0;
        for (int i = 0; i < 16; ++i) {
            if (cards[i] == 2) {
                result++;
                found = i + 1;
            }
        }
        if (result == 0)
            cout << "Volunteer cheated!";
        else if (result == 1)
            cout << found;
        else
            cout << "Bad magician!";
        cout << endl;
    }
}
