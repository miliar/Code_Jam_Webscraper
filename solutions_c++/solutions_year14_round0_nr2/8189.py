#include <iostream>
#include <iomanip>
#include <fstream>

void solve(std::ifstream &input, std::ofstream &output)
{
    long double c, f, x, tNew = 0.0, tOld = 0.0, tFarm = 0.0;
    long double cps = 2.0;
    input >> c >> f >> x;
    tNew = x / cps;
    tOld = tNew + 1;
    while (tNew < tOld) {
        tOld = tNew;
        tFarm += c / cps;
        cps += f;
        tNew = tFarm + x / cps;
    }
    output.flags(std::ios::fixed);
    output << std::setprecision(7) << tOld << std::endl;
}

int main()
{
    std::ifstream input("B-large.in.txt");
    std::ofstream output("out.txt");
    size_t t;
    input >> t;
    for (size_t i = 0; i < t; ++i) {
        output << "Case #" << i + 1 << ": ";
        solve(input, output);
    }
    input.close();
    output.close();
    return 0;
}
