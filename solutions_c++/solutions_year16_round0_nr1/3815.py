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

vector<int> dig;
long long ans1;

bool check(long long num) {
    do {
        long long rem = num % 10;
        dig[rem] = 1;
        num = num / 10;
    } while (num > 0);
    for (int i = 0; i < 10; i++) {
        if (!dig[i]) return false;
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        long long a;
        cin >> a;
        if (a == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        } else {
            ans1 = a;
            dig = vector<int>(10, 0);
            while (!check(ans1)) {
                ans1 += a;
            }
            cout << "Case #" << t << ": " << ans1 << endl;
        }
    }
    return 0;
}