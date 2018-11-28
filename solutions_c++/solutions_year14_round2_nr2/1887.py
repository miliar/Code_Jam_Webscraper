#include <iostream>
#include <sstream>
#include <iomanip>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

int main() {
    int T, A, B, K;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> A >> B >> K;
        int count = 0;
        for (int a = 0; a < A; a++) {
            for (int b = 0; b < B; b++) {
                if ((a & b) < K) {
                    count++;
                }
            }
        }
        cout << "Case #" << t << ": " << count << '\n';
    }
    cout << flush;
    return 0;
}