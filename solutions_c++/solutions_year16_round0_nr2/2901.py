#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

#define N 101

bool all_plus(char* words, int n) {
    for (int i = 0; i < n; ++i)
        if (words[i] == '-')
            return false;
    return true;
}

char change(char word) {
    return word == '+' ? '-' : '+';
}

void reverse(char* words, int low, int high) {
    while (low <= high) {
        if (low == high) {
            words[low] = change(words[low]);
        } else {
            std::swap(words[low], words[high]);
            words[low] = change(words[low]);
            words[high] = change(words[high]);
        }
        low += 1, high -= 1;
    }
}

int find_last_minus(char* words, int n) {
    for (int i = n - 1; i >= 0; --i)
        if (words[i] == '-')
            return i;
    return 0;
}

int find_longest_plus(char* words, int n) {
    for (int i = 0; i < n; ++i)
        if (words[i] == '-')
            return i - 1;
    return n - 1;
}

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    char words[101];
    int _case, n, step;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%s", words);
        n = strlen(words);
        step = 0;
        while (!all_plus(words, n)) {
            if (words[0] == '-') {
                int end = find_last_minus(words, n);
                reverse(words, 0, end);
            } else {
                int end = find_longest_plus(words, n);
                reverse(words, 0, end);
            }
            step++;
        }
        printf("Case #%d: %d\n", i, step);
    }
    return 0;
}
