#include <iostream>
#include <iomanip>
#include <map>
#include <cfloat>

int main()
{
    int T;

    std::cin >> T;


    for (int idx = 1; idx <= T; idx ++)
    {
        int X, R, C;
        char winner;
        std::cin >> X;
        std::cin >> R;
        std::cin >> C;

        if (R*C % X > 0)
        {
            std::cout << "Case #" << idx << ": RICHARD" << std::endl;
        }
        else if (R < X && C < X)
        {
            std::cout << "Case #" << idx << ": RICHARD" << std::endl;
        }
        else if (X > 2 && (R < (X / 2 + 1) || C < (X / 2 + 1)))
        {
            std::cout << "Case #" << idx << ": RICHARD" << std::endl;
        }
        else if (X > 6)
        {
            std::cout << "Case #" << idx << ": RICHARD" << std::endl;
        }
        else
            std::cout << "Case #" << idx << ": GABRIEL" << std::endl;
    }

    return 0;
}