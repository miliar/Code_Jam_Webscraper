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
        long long K,C,S;
        cin >> K >> C >> S;
        cout << "Case #" << t << ":";
        for(int i = 0; i < (int)K; i++) {
            long long j = i;
            for (int c = 1; c < C; c++) {
                j = j * K;
            }
            cout << " " << j + 1;
        }
        cout << endl;
    }
    return 0;
}