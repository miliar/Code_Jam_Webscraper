#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <fstream>
#include <cstdint>
#include <queue>
#include <map>
#include <unordered_map>
#include <iostream>

template<typename SolveClass>
class CodejamTests
{
public:
    CodejamTests(const std::string& input, const std::string& output)
    {
        std::ifstream in(input);
        std::ofstream out(output);
        SolveClass obj;

        size_t maxTests = 0;
        in >> maxTests;
        for (size_t test = 1; test <= maxTests; ++test) {
            in >> obj;
            obj.solve();
            out << "Case #" << test << ": " << obj << "\n";
        }
    }
};

class StandingOvation
{
    friend std::istream& operator>>(std::istream& is, StandingOvation& obj);
    friend std::ostream& operator<<(std::ostream& os, const StandingOvation& obj);

    std::vector<size_t> s;
    size_t result;
public:
    void solve()
    {
        result = 0;
        size_t totalPerson = 0;
        for (size_t i = 0; i < s.size(); ++i) {
            if (totalPerson < i && s[i] != 0) {
                const size_t invite = i - totalPerson;
                result += invite;
                totalPerson += invite;
            }
            totalPerson += s[i];
        }
    }
};
std::istream& operator>>(std::istream& is, StandingOvation& obj)
{
    size_t Smax = 0;
    std::string temp;
    is >> Smax >> temp;
    obj.s.resize(Smax + 1);
    for (size_t i = 0; i < temp.size(); ++i) {
        obj.s[i] = temp[i] - '0';
    }
    return is;
}
std::ostream& operator<<(std::ostream& os, const StandingOvation& obj)
{
    os << obj.result;
    return os;
}

int
main()
{
    CodejamTests<StandingOvation> testA("A.in", "A.out");
    return 0;
}
