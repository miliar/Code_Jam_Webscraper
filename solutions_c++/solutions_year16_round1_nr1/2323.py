#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

char words[1001];

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case, n, m, mask;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%s", words);
        n = strlen(words);
        std::vector<char> ret;
        ret.push_back(words[0]);
        for (int j = 1; j < n; ++j) {
            if (words[j] >= ret[0])
                ret.insert(ret.begin(), words[j]);
            else
                ret.push_back(words[j]);
        }
        printf("Case #%d: ", i);
        for (int j = 0; j < ret.size(); ++j)
            putchar(ret[j]);
        puts("");
    }
    return 0;
}
