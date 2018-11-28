#include <stdio.h>
#include <iostream>

using std::string;
using std::cin;
using std::cout;
using std::max;

bool isConsonant(char c) {
    return (c != 'a') && (c != 'e') && (c != 'o') && (c != 'u')  && (c != 'i');
}

long long getRes(string s, int n) {
    long long res = 0;
    bool *w = new bool[s.length()];
    int *sum = new int[s.length() + 1];
    sum++;
    int len = s.length();
    for (int i = 0; i < len; i++)
        w[i] = false;
    s += 'a';
    for (int i = 0; i < len; i++) {
        int j;
        for (j = i; j < len + 1; j++)
            if (!isConsonant(s[j]))
                break;

        for (int k = i; k < j - n + 1; k++)
            w[k] = true;

        i = j;
    }

    sum[-1] = 0;
    for (int i = 0; i < len; i++)
        sum[i] = sum[i - 1] + w[i];

    for (int i = 0; i < len; i++) {
        int left = i;
        int right = len;
        while (left < right - 1)
            if (sum[(left + right) / 2] - sum[i - 1] == 0)
                left = (left + right) / 2;
            else
                right = (left + right) / 2;

        if (w[left])
            right = left;

        res += max(0, len - right - n + 1);
    }

    return res;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string s;
        int n;
        cin >> s >> n;
        printf("Case #%d: %lld\n", i, getRes(s, n));
    }
    return 0;
}
