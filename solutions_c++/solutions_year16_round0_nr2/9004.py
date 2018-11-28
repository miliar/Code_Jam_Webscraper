#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int solve(string &s) {
    const int len = s.length();
    int count = 0;
    int end = len - 1;

    while (s[end] == '+') {
        --end;
    }

    while (end >= 0) {
        int start = 0;
        while (start <= end && s[start] == '-') {
            ++start;
        }

        if (start == 0) {
            while (start <= end && s[start] == '+') {
                s[start] = '-';
                ++start;
            }
            ++count;
            continue;
        }

        for (int j = 0, k = end; j < k; ++j, --k) {
            swap(s[j], s[k]);
        }
        for (int j = 0; j <= end; ++j) {
            if (s[j] == '-') {
                s[j] = '+';
            } else {
                s[j] = '-';
            }
        }

        end -= start;
        ++count;
    }

    return count;
}

int main()
{
    int N;
    string s;

    scanf("%d", &N);

    for (int i = 1; i <= N; ++i) {
        cin >> s;
        printf("Case #%d: %d\n", i, solve(s));
    }
    return 0;
}
