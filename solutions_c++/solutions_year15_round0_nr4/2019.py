#include <iostream>

enum class Solution
{
    NO_FILL,
    HAS_FILL
};

Solution solve(int x, int r, int c)
{
    if (x == 1)
    {
        return Solution::HAS_FILL;
    }
    else if (x == 2)
    {
        if (r % 2 == 0 || c % 2 == 0)
            return Solution::HAS_FILL;
        return Solution::NO_FILL;
    }
    else if (x == 3)
    {
        static bool has_fill[4][4] = {
            //  1  ,   2  ,   3  ,   4
   /* 1 */  { false, false, false, false },
   /* 2 */  { false, false, true, false },
   /* 3 */  { false, true,  true, true },
   /* 4 */  { false, false, true, false }
        };
        return has_fill[r - 1][c - 1] ? Solution::HAS_FILL : Solution::NO_FILL;
    }
    else if (x == 4)
    {
        static bool has_fill4[4][4] = {
            //  1  ,   2  ,   3  ,   4
   /* 1 */  { false, false, false, false },
   /* 2 */  { false, false, false, false },
   /* 3 */  { false, false, false, true },
   /* 4 */  { false, false, true, true }
        };
        return has_fill4[r - 1][c - 1] ? Solution::HAS_FILL : Solution::NO_FILL;
    }
}

int main()
{
    int t;
    std::cin >> t;

    for (int i = 0; i < t; ++i)
    {
        int x, r, c;
        std::cin >> x >> r >> c;
        auto s = solve(x, r, c);
        std::cout << "Case #" << (i + 1) << ": ";
        if (s == Solution::HAS_FILL)
            std::cout << "GABRIEL\n";
        else
            std::cout << "RICHARD\n";
    }
    return 0;
}
