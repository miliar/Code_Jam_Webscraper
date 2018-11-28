#include <iostream>
#include <fstream>
#include <string>
#include <set>

std::string last_number(int N);

int main()
{
    // In & out.
    std::ifstream in;
    std::ofstream out;

    // Open files.
    in.open("A-small-attempt0.in");
    out.open("A-small-attempt0.out");

    // Global variables.
    int T, N;
    in >> T;
    for(int t = 0; t < T; t ++)
    {
        in >> N;
        out << "Case #" << t + 1 << ": " << last_number(N) << std::endl;
    }
    // Close files.
    out.close();
    in.close();

    return 0;
}


std::string last_number(int N)
{
    //std::string digits = std::to_string(N);
    std::set<char> digits;

    for(int i = 1; i < 100; i ++)
    {
        std::string current_number = std::to_string(i * N);

        for(int j = 0; j < current_number.length(); j ++)
        {
            digits.insert(current_number[j]);
        }

        if(digits.size() == 10)
        {
            return std::to_string(i * N);
        }
    }
    return "INSOMNIA";
}
