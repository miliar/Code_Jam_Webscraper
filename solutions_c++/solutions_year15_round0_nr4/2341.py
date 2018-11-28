#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
#include <utility>

const char* solve(int x, int r, int c)
{
    assert(1 <= x && x <= 4);
    assert(1 <= r && r <= 4);
    assert(1 <= c && c <= 4);

    if (r > c)
        std::swap(r, c);

    switch (x)
    {
        case 1:
            return "GABRIEL";
        case 2:
            return ((r * c) % 2 == 0) ? "GABRIEL" : "RICHARD";
        case 3:
        {
            std::vector<std::pair<int, int>> v = { {2, 3}, {3, 3}, {3, 4} };
            return std::find(v.begin(), v.end(), std::make_pair(r, c)) == v.end() ?
                "RICHARD" : "GABRIEL";
        }
        case 4:
        {
            std::vector<std::pair<int, int>> v = { {3, 4}, {4, 4} };
            return std::find(v.begin(), v.end(), std::make_pair(r, c)) == v.end() ?
                "RICHARD" : "GABRIEL";
        }
    }

    assert(0);
    return "";
}

int main()
{
    int T;
    std::cin >> T;

    for (int i = 1; i <= T; ++i)
    {
        int x, r, c;
        std::cin >> x >> r >> c;
        std::cout << "Case #" << i << ": " << solve(x, r, c) << '\n';
    }

    std::cout.flush();

    return 0;
}
