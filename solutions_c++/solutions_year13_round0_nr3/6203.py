#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

int fas(int min, int max);
bool palyndrome(int i);
bool square(int i);

std::string status(const std::vector<std::vector<char> >& matrix);
int main()
{
    std::fstream in("in.txt"), out("out.txt");
    std::vector<std::vector<char> > matrix(4, std::vector<char>(4));
    int cases, a, b;
    in >> cases;
    for (int i = 1; i <= cases; ++i)
    {
        in >> a >> b;
        std::cout << "Case #" << i << std::endl;
        out << "Case #" << i << ": " << fas(a, b) << '\n';
        std::cout << std::endl << std::endl;
    }
}

int fas(int min, int max)
{
    int number = 0;
    for (int i = min; i <= max; ++i)
    {
        if (square(i) && palyndrome(i) && palyndrome(sqrt(i)))
        {
            std::cout << i << " " << sqrt(i) << std::endl;
            ++number;
        }
    }
    return number;
}

bool palyndrome(int i)
{
    int n = i;
    int reversed = 0;
    int dig;
    while (n > 0)
    {
         dig = n % 10;
         reversed = reversed * 10 + dig;
         n = n / 10;
    }
    return reversed == i;
}

bool square(int i)
{
    int b = (int) (sqrt((float)i) + 0.5f);
    return b*b == i;
}
