#include <iostream>
#include <string>
#include <vector>
#include <inttypes.h>

typedef int64_t lint;

// 0 1 2 3  4  5  6  7
// 1 i j k -1 -i -j -k

const int mult[8][8] = {
    {0, 1, 2, 3, 4, 5, 6, 7},
    {1, 4, 3, 6, 5, 0, 7, 2},
    {2, 7, 4, 1, 6, 3, 0, 5},
    {3, 2, 5, 4, 7, 6, 1, 0},
    {4, 5, 6, 7, 0, 1, 2, 3},
    {5, 0, 7, 2, 1, 4, 3, 6},
    {6, 3, 0, 5, 2, 7, 4, 1},
    {7, 6, 1, 0, 3, 2, 5, 4}
};

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t;
        int L;
        lint X;
        std::cin >> L >> X;
        if (X > 12)
            X = 12 + X % 12;

        std::vector<int> table(127, 0);
        table['i'] = 1;
        table['j'] = 2;
        table['k'] = 3;

        std::string s;
        std::cin >> s;

        std::vector<int> v(L);
        for (int l = 0; l < L; ++l)
            v[l] = table[s[l]];

        int search = 1;
        int cur = 0;
        for (int x = 0; x < X; ++x) {
            for (int l = 0; l < L; ++l) {
                cur = mult[cur][v[l]];
                if (cur == search) {
                    cur = 0;
                    ++search;
                    if (search == 4) {
                        search = 8;
                    }
                }
            }
        }
        if (search == 8 && cur == 0)
            std::cout << ": YES" << std::endl;
        else
            std::cout << ": NO" << std::endl;
    }
}
