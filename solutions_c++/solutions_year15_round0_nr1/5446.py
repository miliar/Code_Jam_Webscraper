#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
#include <queue>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main() {
    //ifstream cin("in.txt");
    //ofstream cout("out.txt");
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        int result = 0;

        int smax = 0;
        cin >> smax;
        vector<int> snums(smax+1);
        for (int& shy: snums) {
            char c = 0;
            cin >> c;
            shy = c - '0';
        }

        int count = 0;
        for (int i = 0; i <= smax; ++i) {
            if (count < i) {
                result += i - count;
                count += i - count;
            }
            count += snums[i];
        }

        cout << result << endl;
    }
}
