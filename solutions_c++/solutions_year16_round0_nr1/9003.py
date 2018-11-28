#include <iostream>
#include <vector>

using namespace std;

void h(int x, vector<bool> &seen) {
    while (x >= 10) {
        seen[x%10] = true;
        x /= 10;
    }
    if (x > 0) {
        seen[x%10] = true;
    }

}
int solve(int x) {
    vector<bool> seen;
    for (int j = 0; j < 10; j++) {
        seen.push_back(false);
    }
    bool done;
    for (int i = 1; i < 1000; i++) {
        h(x*i,seen);
        done = true;
        for (int j = 0; j < 10; j++) {
            done &= seen[j]; 
        }
        if (done) {
            return x*i;
        }
    }
    return -1;
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        int res = solve(x);
        if (res > 0) {
            printf("Case #%d: %d\n", i+1, res);
        }
        else {
            printf("Case #%d: INSOMNIA\n", i+1);
        }
    }
    return 0;
}
