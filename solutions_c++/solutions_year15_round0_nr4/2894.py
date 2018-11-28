#include <cmath>
#include <iostream>

bool calcul(int X, int R, int C)
{
    if ((R * C) % X)
        return false;
    int w = std::ceil((double)X / 2.0);
    if (w > R || w > C)
        return false;

    if (X <= 3 && X != 0)
        return true;
    else if (X == 4)
        return (R > 2 && C > 2)? true : false;
    return false;
}

int main()
{
    int T = 0;
    std::cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int X = 0, R = 0, C = 0;
        std::cin >> X >> R >> C;
        std::cout << "Case #" << i + 1 << ": ";
        (calcul(X, R, C)) ? std::cout << "GABRIEL" << std::endl : std::cout << "RICHARD" << std::endl;
    }
    return 0;
}
