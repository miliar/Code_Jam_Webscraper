#include <iostream>
#include <iomanip>
#include <fstream>

void solution(std::ifstream &input, std::ofstream &output)
{
    long double c, f, x;
    long double time_new = 0.0;
    long double time_old = 0.0;
    long double time_farm = 0.0;
    long double cps = 2.0;

    //std::cin >> c >> f >> x;
    input >> c >> f >> x;

    time_new = x / cps;
    time_old = time_new + 1;

    while (time_new < time_old) {
        time_old = time_new;
        time_farm += c / cps;
        cps += f;
        time_new = time_farm + x / cps;
    }

    //std::cout.flags(std::ios::fixed);
    //std::cout << std::setprecision(7) << time_old << std::endl;
    output.flags(std::ios::fixed);
    output << std::setprecision(7) << time_old << std::endl;

}

int main()
{
    std::ifstream input("B-large.in");
    std::ofstream output("out.txt");
    size_t t;

    input >> t;

    for (size_t i = 0; i < t; ++i) {
        output << "Case #" << i + 1 << ": ";
        solution(input, output);
    }

    input.close();
    output.close();

    return 0;
}
