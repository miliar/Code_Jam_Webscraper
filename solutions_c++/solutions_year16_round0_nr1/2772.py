#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
using namespace std;

void updateDigits(int n, bool a[]) {
    if (n == 0) {
        a[0] = true;
        return;
    }
    while (n > 0) {
        a[n%10] = true;
        n /= 10;
    }
    return;
}

bool allFound(bool a[]) {
    bool res = true;
    for (int i = 0; i < 10; i++) {
        res &= a[i];
    }
    return res;
}

int main() {
    //    freopen("input.txt", "rt", stdin);
    //    freopen("output.txt", "wt", stdout);
    //ios::sync_with_stdio(false);

    int T;
    cin >> T;
    
    for (int i = 1; i <= T; i++) {
        int N;
        cin >> N;
        
        if (N == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        
        int count = 0;
        
        bool a[10];
        for (int i = 0; i < 10; i++) {
            a[i] = false;
        }
        
        while (!allFound(a)) {
            count += N;
            updateDigits(count, a);
        }
        
        cout << "Case #" << i << ": " << count << endl;
        
    }
    return 0;
}

