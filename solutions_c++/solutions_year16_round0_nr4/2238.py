#include <stdint.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main()
{
    int T, K, C, S;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> K >> C >> S;
        cout << "Case #" << (i + 1) << ": ";
        for (int j = 1; j <= S; ++j) {
            if (j < S) cout << j << " ";
            else cout << j;
        }
        cout << endl;
    }
    return 0;
}
