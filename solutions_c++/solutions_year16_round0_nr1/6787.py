#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    int test_case;
    cin>>test_case;
    int case_num = 0;
    while (test_case--) {
        case_num++;
        long long n;
        cin>>n;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", case_num);
            continue;
        }
        vector <bool> visited(10, false);
        long long i = 1;
        int cnt = 0;
        while (1) {
            long long cur = n * i, cur_re = cur;
            while (cur) {
                int digit = cur % 10;
                cur = (cur - digit) / 10;
                if (!visited[digit]) {
                    visited[digit] = true;
                    cnt++;
                }
            }
            if (cnt >= 10) {
                printf("Case #%d: %d\n", case_num, cur_re);
                break;
            }
            i++;
        }
    }
    return 0;
}
