#include <iostream>
#include <sstream>
#include <set>
#include <list>

typedef std::list<char> OutType;

void function(const std::string& in, OutType& out)
{
    for (auto datum : in)
    {
        if (datum < out.front())
        {
            out.push_back(datum);
        }
        else
        {
            out.push_front(datum);
        }
    }

}


int main()
{
    int T;

    std::cin >> T;
    for (auto i = 0; i < T; i++)
    {
        OutType out;
        std::string data;
        std::cin >> data;
        function(data, out);


        std::cout << "Case #" << i + 1 << ": ";
        for (auto character : out)
        {
            std::cout << character;
        }
        std::cout << std::endl;

    }

    return 0;
}