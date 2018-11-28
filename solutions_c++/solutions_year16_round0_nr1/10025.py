#include <iostream>
#include <fstream>
#include <set>

int parseDigits(int n, std::set<int> &s)
{
    while (n >= 1)
    {
        s.insert(n % 10);
        n /= 10;
    }

    return s.size();
}

int calculateCase(int n)
{
    if (n == 0)
        return -1;

    std::set<int> s;

    int i = 1;
    while (true)
    {
        if (parseDigits(i * n, s) >= 10)
            return i * n;

        ++i;
    }

    return -1;
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <input data>" << std::endl;
        return 1;
    }

    std::ifstream f(argv[1]);
    if (!f)
    {
        std::cerr << "Error: can't open " << argv[1] << std::endl;
        return 2;
    }

    size_t caseCount = 0;
    f >> caseCount;
    for (size_t i = 0; i < caseCount; ++i)
    {
        int n = 0;
        f >> n;
        int result = calculateCase(n);

        std::cout << "Case #" << (i + 1) << ": ";

        if (result < 0)
            std::cout << "INSOMNIA";
        else
            std::cout << result;

        std::cout << std::endl;
    }


    f.close();
    return 0;
}
