#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;

    for (t = 1; t <= T; ++t) {
        int K, C, S;
        cin >> K >> C >> S;

        printf("Case #%d:", t);
        for (int i = 0; i < K; ++i) {
            printf(" %d", i + 1);
        }
        printf("\n");
    }

    return 0;
}
