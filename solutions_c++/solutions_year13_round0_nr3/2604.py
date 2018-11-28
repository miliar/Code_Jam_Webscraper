#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int p[] = {1, 4, 9, 121, 484};

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        cout << "Case #" << c << ": ";
        
        int A, B, count = 0;
        cin >> A >> B;
        for (int i = 0; i < 5; i++) {
            if (p[i] >= A && p[i] <= B) {
                count++;
            }
        }
        
        cout << count << endl;
    }
    
    return 0;
}
