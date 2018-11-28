#include <iostream>
#include <stdint.h> // uint_fast64_t
#include <string>
#include <cassert>
#include <limits>
#include <iomanip>

using namespace std;

int smallest_number_of_times_to_get_all_pancakes_happy_side_up (const std::string& stack)
{
    int smallest_number_of_flips = 0;
    char last = '+';
    for (int i = stack.size()-1; i >=0; --i )
    {
        char c = stack[i];
        assert (c=='-' || c=='+');
        if (c != last)
        {
            last = c;
            smallest_number_of_flips++;
        }
    }
    return smallest_number_of_flips;

}

int main()
{
    int t;
    std::cin >> t;
    assert(1 <= t);
    assert(     t <= 100);

    for (int i=1; i<=t; ++i)
    {
        std::cout <<"Case #"<< i <<": ";

        std::string stack_of_pancakes;
        std::cin >> stack_of_pancakes;

        auto n = smallest_number_of_times_to_get_all_pancakes_happy_side_up (stack_of_pancakes);

        std::cout << n << std::endl;
    }
}
