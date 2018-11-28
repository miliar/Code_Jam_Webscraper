#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

const int N = 1005;
char shy[N];

int main () {
//    freopen("A-large.in", "r" ,stdin);
//    freopen("out.txt", "w", stdout);
    int cases;
    cin >> cases;
    int S;
    for (int cas = 1; cas <= cases; cas ++) {
        scanf ("%d", &S);
        scanf ("%s", shy);
        int ans = 0;
        int sum = 0;
        for (int i = 0; i <= S; i++) {
            if (shy[i] == '0') continue;
            if (sum < i) {
                ans += i - sum;
                sum = i;
                sum += shy[i] - '0';
            }
            else {
                sum += shy[i] - '0';
            }
        }
        printf ("Case #%d: %d\n", cas, ans);
    }

    return  0;
}
