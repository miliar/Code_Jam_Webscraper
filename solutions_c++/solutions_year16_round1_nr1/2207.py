#include <algorithm>
#include <bitset>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <limits>
#include <list>
#include <numeric>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

char buf[1001];

int main(int argc, const char *argv[]) {
    freopen("A_A.in", "r", stdin);
    freopen("A_A.out", "w", stdout);
    size_t t = 0;
    scanf("%zd", &t);
    for (size_t i = 1; i <= t; ++i) {
        scanf("%s", buf);
        size_t len = strlen(buf);
        list<char> result;
        result.push_back(buf[0]);
        for (size_t j = 1; j < len; ++j) {
            bool to_front = true;
            for (auto p = result.cbegin(); p != result.cend(); ++p) {
                if (*p != buf[j]) {
                    to_front = *p < buf[j];
                    break;
                }
            }
            if (to_front) {
                result.push_front(buf[j]);
            } else {
                result.push_back(buf[j]);
            }
        }
        printf("Case #%zd: ", i);
        for (auto &c : result) {
            printf("%c", c);
        }
        printf("\n");
    }
    return EXIT_SUCCESS;
}
