#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;



int main() {
    //freopen("a-in.txt", "r", stdin);
    //freopen("a-out.txt", "w", stdout);
    int cases;
    cin >> cases;
    for (int t = 1; t <= cases; t++)
    {
        int sm;
        string str;
        cin >> sm >> str;
        int sum = 0;
        int needed = 0;
        for (int i = 0; i <= sm; i++) {
            if (str[i] > '0') {
                if (sum < i) {
                    needed += i - sum;
                    sum = i + str[i] - '0';
                } else {
                    sum += str[i] - '0';
                }

            }
        }
        printf("Case #%d: %d\n", t, needed);
    }
    return 0;
}