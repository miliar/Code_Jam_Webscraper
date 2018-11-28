#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

int solve() {
    string str;
    cin >> str;

    reverse(str.begin(), str.end());
    int n = str.length();
    char next = '+';
    int ans = 0;

    for (int i = 0; i != n; ++i) {
        if (str[i] != next) {
            ++ans;
            next = next == '+' ? '-' : '+';
        }
    }

    return ans;
}

int main() {
    freopen("C:\\Users\\timur\\Downloads\\B-large.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int test = 0; test != t; ++test) {
        printf("Case #%d: %d\n", test + 1, solve());
    }

    return 0;
}