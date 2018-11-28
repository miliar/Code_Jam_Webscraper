#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>

const long long INF = 1000000000000000LL;

std::vector<long long> element;
int n;

bool judge(long long x) {
    std::string string;
    std::stringstream buffer;
    buffer << x;
    buffer >> string;
    for (int i = 0; i << 1 < string.length(); ++ i) {
        if (string[i] != string[string.length() - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    for (int i = 0; i <= 1000000; ++ i) {
        long long x = (long long)i * i;
        if (judge(x) && judge(i)) {
            element.push_back(x);
        }
    }
/*
    for (int i = 0; i < element.size(); ++ i) {
        printf("%lld\n", element[i]);
    }
    printf("%d\n", element.size());
*/
    int test_count;
    scanf("%d", &test_count);
    for (int t = 1; t <= test_count; ++ t) {
        long long a, b;
        std::cin >> a >> b;
        int x = std::upper_bound(element.begin(), element.end(), a - 1) - element.begin();
        int y = std::upper_bound(element.begin(), element.end(), b) - element.begin();
        printf("Case #%d: %d\n", t, y - x);
    }
    return 0;
}
