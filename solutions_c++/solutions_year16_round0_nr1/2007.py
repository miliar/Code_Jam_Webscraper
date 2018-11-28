#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

bool good[15];
int num;

void go(int casenum) {
    int n;
    memset(good, 0, sizeof(good));
    num = 0;
    cin >> n;
    if (n == 0) {
        cout << "Case #" << casenum << ": INSOMNIA\n";
        return;
    }
    
    for (int i = 1; 1; i++) {
        int k = n * i;
        while (k) {
            if (!good[k % 10]) good[k % 10] = 1, num++;
            k /= 10;
        }
        if (num == 10) {
            cout << "Case #" << casenum << ": " << n * i << '\n';
            return;
        }
    }
}

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) go(i);
}
