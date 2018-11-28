#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; ++t) {
        double c, f, x;
        cin >> c >> f >> x;
        double s = 0;
        double r = 2.0;
        double prev, cur;
        do {
            prev = s + x / r;
            s += c / r;
            r += f;
            cur = s + x / r;
        } while (prev > cur);
        cout.precision(7);
        cout << fixed << "Case #" << t << ": " << prev << endl;
    }
    
    
    return 0;
}