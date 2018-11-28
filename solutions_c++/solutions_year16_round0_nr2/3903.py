#include <algorithm>
#include <bitset>
#include <cmath>
#include <fstream>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string str;
        cin >> str;
        int ans1 = 0;
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str[i] == '-') {
                ans1++;
                for (int j = i - 1; j >= 0; j--) {
                    if (str[j] == '-') {
                        str[j] = '+';
                    } else {
                        str[j] = '-';
                    }
                }
            }
        }
        cout << "Case #" << t << ": " << ans1 << endl;
    }
    return 0;
}