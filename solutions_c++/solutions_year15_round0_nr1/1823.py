#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace  std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int t, s;
    string str;

    cin >> t;
    for(int k = 1; k <= t; k ++) {
        cin >> s >> str;
        int res = 0, sum = 0;
        for(int i = 0; i < str.size(); i ++) {
            if(sum < i) {
                res += (i - sum);
                sum = i;
            }
            sum += (str[i] - '0');
        }
        cout << "Case #" << k << ": " << res << endl;
    }
    return 0;
}
