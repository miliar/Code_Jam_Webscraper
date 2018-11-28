#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <complex>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

int main() {
    int T;
    cin >> T;
    vector<vector<int> > f1(4, vector<int>(4));
    vector<vector<int> > f2(4, vector<int>(4));
    for (int t = 1; t <= T; ++t) {
        int a, b;
        cin >> a;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> f1[i][j];
            }
        }
        cin >> b;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> f2[i][j];
            }
        }
        int count = 0;
        int num = 0;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (f1[a-1][i] == f2[b-1][j]) {
                    num = f1[a-1][i];
                    ++count;
                    break;
                }
            }
        }
        if (count == 0) {
            cout << "Case #" << t << ": Volunteer cheated!" << endl;
        } else if (count > 1) {
            cout << "Case #" << t << ": Bad magician!" << endl;
        } else {
            cout << "Case #" << t << ": " << num << endl;
        }
    }

    return 0;
}