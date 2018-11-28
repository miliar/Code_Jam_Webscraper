#include <iostream>
#include <fstream>
#include <array>
#include <cassert>

using val = int64_t;

std::tuple<val, val> pop_digit(val value)
{
    val result = value / 10;
    return std::make_tuple(result, value - result * 10);
}

val find_last(const val n)
{
    val total = 0;
    std::array<bool, 10> seen = {};
    do
    {
        total += n;

        val current = total;
        while(current != 0)
        {
            val digit;
            std::tie(current, digit) = pop_digit(current);
            assert(digit < 10);
            seen[digit] = true;
        }
    }
    while(std::find(seen.begin(), seen.end(), false) != seen.end());

    return total;
}

int main()
{
    std::ifstream input;
    input.open("/Users/stammerj/playground/jam/sheep/large0", std::ifstream::in);
    assert(input.good());
    
    size_t cases;
    input >> cases;
    for (size_t i = 0; i < cases; ++i)
    {
        val n;
        input >> n;

        std::cout << "Case #" << (i + 1) << ": ";
        if (n == 0)
            std::cout << "INSOMNIA";
        else
            std::cout << find_last(n);

        std::cout << std::endl;
    }
}