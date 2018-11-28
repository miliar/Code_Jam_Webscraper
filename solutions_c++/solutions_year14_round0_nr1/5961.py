#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void run() {
    int row[2];
    int cards[2][4][4];
    for (int i = 0; i < 2; i++) {
        cin >> row[i];
        for (int y = 0; y < 4; y++) {
            for (int x = 0; x < 4; x++) {
                cin >> cards[i][y][x];
            }
        }
    }
    vector<int> answers;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (cards[0][row[0] - 1][i] == cards[1][row[1] - 1][j]) {
                answers.push_back(cards[0][row[0] - 1][i]);
            }
        }
    }
    if (answers.size() == 1) {
        cout << answers.front() << endl;
    } else if (answers.size() > 1) {
        cout << "Bad magician!" << endl;
    } else {
        cout << "Volunteer cheated!" << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        run();
    }
}
