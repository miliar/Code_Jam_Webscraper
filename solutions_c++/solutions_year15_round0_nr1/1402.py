#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

#define N 1005

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int kase, n, answer, stood_up;
    char shyness[N];

    scanf("%d", &kase);
    for (int kase_no = 1; kase_no <= kase; kase_no++) {
        scanf("%d %s", &n, shyness);
        stood_up = answer = 0;

        if (shyness[0] == '0') {
            stood_up = 1;
            answer += 1;
        }
        else
            stood_up = shyness[0] - '0';

        for (int i = 1; i <= n; i++) {
            if (stood_up < i) {
                answer += i - stood_up;
                stood_up += i - stood_up;
            }
            stood_up += shyness[i] - '0';
        }
        printf("Case #%d: %d\n", kase_no, answer);
    }
    return 0;
}
