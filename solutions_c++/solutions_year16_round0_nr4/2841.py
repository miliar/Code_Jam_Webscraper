#include <iostream>
#include <string>
#include <sstream>
#include <set>
typedef long long Number;

Number myPow(const Number nro, const Number exponent)
{
    Number result = 1;
    for (int i = 0; i < exponent; ++i)
    {
        result *=  nro;
    }
    return result;
}
void findPosible(const Number K, const Number C, const Number S)
{
    for (Number index = 0; index < K; ++index)
    {
        const Number position = index*myPow(K, C-1) + 1;
        std::cout << " " << position;
    }
}

int main()
{
    int T;

    std::cin >> T;
    for (auto i = 0; i < T; i++)
    {

        Number K;
        Number C;
        Number S;

        std::cin >> K;
        std::cin >> C;
        std::cin >> S;


        std::cout << "Case #" << i + 1 << ":";
        findPosible(K, C, S);
        std::cout << std::endl;
    }

    return 0;
}